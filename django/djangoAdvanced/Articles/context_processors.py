from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    if not request.user.is_authenticated:
        return {"form_login": AuthenticationForm()}
    return {}