from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50, required=False)
    last_name = forms.CharField(label='Last name', max_length=50, required=False)
    email = forms.EmailField(label='Email', required=False)
    phone_number = forms.CharField(label='Phone', required=False)
    address = forms.CharField(label='Address',required=False, max_length=100)
