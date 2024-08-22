from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path('ws/message/chat/<slug:group_name>', consumer.MessageConsumer.as_asgi()),
]
