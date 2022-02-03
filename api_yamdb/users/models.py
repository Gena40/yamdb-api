from django.contrib.auth.models import AbstractUser
from django.db import models
import enum


class Roles(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'


class User(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=ROLES,
        default='user'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique user email'
            ),
        )

    @property
    def is_administrator(self):
        return self.role == Roles.ADMIN.value

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR.value
