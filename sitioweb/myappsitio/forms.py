# forms.py
from django import forms

class LoginForm(forms.Form):
    correo = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)


