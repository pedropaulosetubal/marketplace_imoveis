from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
