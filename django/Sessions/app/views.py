from django.shortcuts import render
from django.conf import settings
import random

def index(request):
    request.session.clear_expired()
    request.session.set_expiry(42)
    if 'username' not in request.session:
        request.session['username'] = random.choice(settings.USER_NAMES) 
    username = request.session['username']           

    return render(request, 'ex/index.html', {"username": username})