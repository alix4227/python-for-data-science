import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import re

from .models import Chatroom, Message,User

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def get_messages(self):
        chatroom = Chatroom.objects.get(name=self.room_name)
        return list(Message.objects.filter(chatroom=chatroom).order_by('created').values('user__username', 'content'))
    
    @database_sync_to_async
    def get_members_connected(self):
        chatroom = Chatroom.objects.get(name=self.room_name)
        return list(chatroom.members.values_list('username', flat=True))

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = re.sub(r'[^a-zA-Z0-9\-_\.]', '_', self.room_name)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.save_connected_members()
        messages = await self.get_messages()
        members_connected = await self.get_members_connected()
        messages = [f"{message['user__username']}: {message['content']}" for message in messages][-3:]
        await self.send(
            text_data=json.dumps(
                {
                    "messages": messages,
                    "members_connected": members_connected,
                }
            )
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": f"{self.scope['user']} has joined the chat",
                "members_connected": members_connected,
            }
        )

    async def disconnect(self, close_code):
        await self.remove_connected_members()
        members_connected = await self.get_members_connected()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": f"{self.scope['user']} has left the chat",
                "members_connected":members_connected,
            }
        )
        # Leave room group after broadcasting the departure.
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.save_message(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": f"{self.scope['user']}: {message}"}
        )

    @database_sync_to_async
    def save_message(self, message):
        chatroom = Chatroom.objects.get(name=self.room_name)
        Message.objects.create(
            user=self.scope["user"],
            chatroom=chatroom,
            content=message,
        )
    @database_sync_to_async
    def save_connected_members(self):
        chatroom = Chatroom.objects.get(name=self.room_name)
        chatroom.members.add(self.scope["user"])
    @database_sync_to_async
    def remove_connected_members(self):
        chatroom = Chatroom.objects.get(name=self.room_name)
        chatroom.members.remove(self.scope["user"])
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "messages": event.get("messages", []),"members_connected": event.get("members_connected", []),}))