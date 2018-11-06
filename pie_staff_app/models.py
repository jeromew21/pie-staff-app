from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PieUserManager(BaseUserManager):
    def create_user(self, **kwargs):
        print(kwargs)
        user = self.model(
            email=kwargs['email'],
            username=kwargs['username']
        )
        user.save()
        return user

class PieUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    username = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    objects = PieUserManager()
    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        return True

class Snippet(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=255)
    author = models.ForeignKey("PieUser", on_delete=models.DO_NOTHING)