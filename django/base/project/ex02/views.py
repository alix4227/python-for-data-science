from django.shortcuts import render, redirect
from django.utils import timezone
from ex02.forms import LoginForm
from django.conf import settings
import os
def form(request):
    title = 'Text Area'
    logs = []
    if os.path.exists(settings.LOG_FILE):
        with open(settings.LOG_FILE, 'r') as file2:
            logs = file2.readlines()
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
      
        if MyLoginForm.is_valid():
            text = MyLoginForm.cleaned_data['text']
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(settings.LOG_FILE, 'a') as file:
                file.write(f"[{timestamp}]{text+'\n'}")
            with open(settings.LOG_FILE, 'r') as file2:
                logs = file2.readlines()
            MyLoginForm = LoginForm()
            return redirect('form')
    else:
        MyLoginForm = LoginForm()
    return render(request, 'ex02/form.html', {"title": title, "form": MyLoginForm, "logs": logs})