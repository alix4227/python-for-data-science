from django.shortcuts import render
from django.conf import settings
from app.forms import LoginForm
from app.models import User
import random

def index(request):
    request.session.clear_expired()
    request.session.set_expiry(42)
    if 'username' not in request.session:
        request.session['username'] = random.choice(settings.USER_NAMES) 
    username = request.session['username']           

    return render(request, 'ex/index.html', {"username": username})

def subscribe(request):
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_verification = request.POST.get('password_verification')
        if (password != password_verification):
            return render(request, 'ex/subscribe.html', {"username": username})
        myForm = LoginForm(request.POST)
        if myForm.is_valid():
            if User.objects.filter(username=username).exists():
                return render(request, 'ex/subscribe.html', {"username": username})
            User.objects.create_user(username=username, password=password)           
    return render(request, 'ex/subscribe.html', {"username":''})

def login(request):
             
    username= 'Alix'
    return render(request, 'ex/login.html', {"username": username})