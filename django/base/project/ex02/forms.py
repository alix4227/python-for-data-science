from django import forms

class LoginForm(forms.Form):
   text = forms.CharField(
        widget=forms.Textarea(attrs={
            'style': 'margin-left:20%; height:80px; font-size:16px;',
            'rows': '5',
            'cols': '40'
            
        }))
