from django.db import models
from .managers import CostumeUserManager
from django.contrib.auth.models import AbstractBaseUser


user_color = (
    ('slate', 'slate'),
    ('neutral', 'neutral'),
    ('red', 'red'),
    ('orange', 'orange'),
    ('lime', 'lime'),
    ('green', 'green'),
    ('teal', 'teal'),
    ('sky', 'sky'),
    ('indigo', 'indigo'),
    ('purple', 'purple'),
    ('fuchsia', 'fuchsia'),
    ('pink', 'pink'),
    ('rose', 'rose')
)


class CostumeUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=user_color, null=True, blank=True)
    objects = CostumeUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


