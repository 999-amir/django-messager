from django.db import models
from account.models import CostumeUser


class GroupModel(models.Model):
    name = models.CharField(max_length=40, unique=True)
    user = models.ManyToManyField(CostumeUser, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MessageModel(models.Model):
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CostumeUser, on_delete=models.CASCADE)
    message = models.TextField(max_length=250)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.group} - {self.user}'

