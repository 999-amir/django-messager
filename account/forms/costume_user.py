from django import forms
from ..models import CostumeUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CostumeUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='password')

    class Meta:
        model = CostumeUser
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CostumeUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='want to change password? <a href="../password/">click here</a>')

    class Meta:
        model = CostumeUser
        fields = ('username',)