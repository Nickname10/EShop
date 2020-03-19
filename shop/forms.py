from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=50)

    def clean_confirm_password(self):
        data = self.cleaned_data
        if data['password'] == data['confirm_password']:
            return data['password']
        else:
            raise ValidationError("Пароли не совпадают")


