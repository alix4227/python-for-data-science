import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import re

from .models import Chatroom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = re.sub(r'[^a-zA-Z0-9\-_\.]', '_', self.room_name)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": f"{self.scope['user']} has joined the chat"}
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.save_message(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    @database_sync_to_async
    def save_message(self, message):
        chatroom = Chatroom.objects.get(name=self.room_name)
        Message.objects.create(
            user=self.scope["user"],
            chatroom=chatroom,
            content=message,
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))