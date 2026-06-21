from django import forms
from .models import Tip

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ["contenu"]