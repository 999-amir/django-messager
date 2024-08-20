from django.urls import path
from . import views


app_name = 'message'

urlpatterns = [
    path('group/', views.GroupView.as_view(), name='group'),
    path('chat/<slug:group_name>', views.MessageView.as_view(), name='chat'),
]
