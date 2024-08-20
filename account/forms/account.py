from django import forms
from ..models import CostumeUser


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=250)
