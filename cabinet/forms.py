from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from shop.models import Item


class UserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50, required=False)
    last_name = forms.CharField(label='Last name', max_length=50, required=False)
    email = forms.EmailField(label='Email', required=False)
    phone_number = forms.CharField(label='Phone', required=False)
    address = forms.CharField(label='Address', required=False, max_length=100)


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['Brand', 'title', 'short_description', 'long_description', 'isNewCollection',
                  'price']
        labels = {

            'Brand': _('brand'),
            'title': _('title'),
            'short_description': _('short description'),
            'long_description': _('long description'),
            'isNewCollection': _('is it new collection'),
        }
        help_texts = {
            'image': _('upload item image'),
        }
        error_messages = {
            'image': {
                'max_length': _("This writer's name is too long."),
            },
        }
