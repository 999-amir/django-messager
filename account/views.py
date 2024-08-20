from django.shortcuts import render, redirect
from django.views import View
from .forms.account import CreateUserForm
from .models import CostumeUser
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import random

user_color = ['slate', 'neutral', 'red', 'orange', 'lime', 'green', 'teal', 'sky', 'indigo', 'purple', 'fuchsia',
              'pink', 'rose']


class UserView(View):
    forms = CreateUserForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('message:group')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {
            'forms': self.forms()
        }
        return render(request, 'account/user.html', context)

    def post(self, request):
        forms = self.forms(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            if CostumeUser.objects.filter(username=cd['username']).exists():
                user = authenticate(request, username=cd['username'], password=cd['password'])
                if user is not None:
                    # available username with correct password for login
                    login(request, user)
                    messages.success(request, f'welcome back user-{user.id}', 'blue-600')
                    return redirect('message:group')
                else:
                    # available username but wrong password for login
                    messages.error(request, 'wrong password', 'red-600')
                    return render(request, 'account/user.html', {'forms': forms})
            else:
                # unavailable username -> create new user
                user = CostumeUser.objects.create_user(username=cd['username'], password=cd['password'])
                user.color = random.choice(user_color)
                user.save()
                login(request, user)
                messages.success(request, f'hello user-{user.id}', 'blue-600')
                return redirect('message:group')
        # form is incorrect
        messages.warning(request, 'form is incorrect', 'orange-600')
        return render(request, 'account/user.html', {'forms': forms})
