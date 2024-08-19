from django.shortcuts import render
from django.views import View


class MessageView(View):
    def get(self, request):
        return render(request, 'message/text-returner.html')
