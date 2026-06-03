from django.shortcuts import render
from django.utils import timezone
from ex02.forms import LoginForm
def form(request):
    title = 'Text Area'
    if request.method == "POST":
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
        text = MyLoginForm.cleaned_data['text']
        timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        with open("ex02/logs.txt", 'a') as file:
            file.write(f"[{timestamp}]{text+'\n'}")

    else:
        MyLoginForm = LoginForm()
    return render(request, 'ex02/form.html', {"title": title, "form": MyLoginForm})