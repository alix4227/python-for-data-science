from django.shortcuts import render
from ex02.forms import LoginForm
def form(request):
    title = 'Text Area'
    if request.method == "POST":
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
        text = MyLoginForm.cleaned_data['text']
        with open("ex02/logs.py", 'w') as file:
            file.write(text)

    else:
        MyLoginForm = LoginForm()
    return render(request, 'ex02/form.html', {"title": title, "form": MyLoginForm})