from channels.generic.websocket import WebsocketConsumer
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .models import GroupModel, MessageModel
import json
from asgiref.sync import async_to_sync


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.group = get_object_or_404(GroupModel, name=self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        if self.user not in self.group.online_user.all():
            self.group.online_user.add(self.user)
            self.online_user()
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        if self.user in self.group.online_user.all():
            self.group.online_user.remove(self.user)
            self.online_user()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        chat = MessageModel.objects.create(user=self.user, group=self.group, message=message)
        event = {
            'type': 'chat_handler',
            'chat_id': chat.id
        }
        async_to_sync(self.channel_layer.group_send)(self.group_name, event)

    def chat_handler(self, event):
        chat_id = event['chat_id']
        chat = MessageModel.objects.get(id=chat_id)
        context = {
            'chat': chat,
            'chats': MessageModel.objects.filter(group=self.group)
        }
        self.send(render_to_string('message/htmx/chat-message.html', context))

    def online_user(self):
        event = {
            'type': 'online_user_handler',
            'online_user_number': self.group.online_user.count()
        }
        async_to_sync(self.channel_layer.group_send)(self.group_name, event)

    def online_user_handler(self, event):
        online_user_number = event['online_user_number']
        context = {
            'online_user_number': online_user_number
        }
        self.send(render_to_string('message/htmx/online_user_number.html', context))
