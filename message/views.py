from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import MessageModel, GroupModel
from .forms import MessageForm
from django.shortcuts import get_object_or_404


class GroupView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'no-permission', 'red-600')
            return redirect('user:create_or_login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        groups = GroupModel.objects.filter(user=request.user)
        context = {
            'groups': groups
        }
        return render(request, 'message/groups.html', context)


class MessageView(View):
    form_class = MessageForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'need authentication', 'red-600')
            return redirect('user:create_or_login')
        elif not GroupModel.objects.filter(user=request.user, name=kwargs['group_name']).exists():
                messages.error(request, 'group is unavailable or unreachable', 'red-600')
                return redirect('message:group')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, group_name):
        chats = MessageModel.objects.filter(group__name=group_name)
        form = self.form_class()
        context = {
            'group_name': group_name,
            'chats': chats,
            'form': form
        }
        return render(request, 'message/message.html', context)

    def post(self, request, group_name):
        form = self.form_class(request.POST)
        if form.is_valid():
            MessageModel.objects.create(user=request.user, group=get_object_or_404(GroupModel, name=group_name), message=form.cleaned_data['message'])
        chats = MessageModel.objects.filter(group__name=group_name).order_by('-created')
        context = {
            'group_name': group_name,
            'chats': chats,
            'form': form
        }
        return render(request, 'message/message.html', context)

