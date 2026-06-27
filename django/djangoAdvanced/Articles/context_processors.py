from .forms import CustomAuthenticationForm

def login_form(request):
    if not request.user.is_authenticated:
        return {"form_login": CustomAuthenticationForm()}
    return {}