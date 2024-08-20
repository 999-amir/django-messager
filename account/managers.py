from django.contrib.auth.models import BaseUserManager


class CostumeUserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('!!! username needed !!!')
        user = self.model(username=self.normalize_email(username))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
