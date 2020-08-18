"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from abjhelp.utils.models import AbjHelpModel

class User(AbjHelpModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese email.'
        }
    )

    first_name = models.CharField('first name', max_length=150, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username

    class Meta:
        """Meta class."""

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class HelpRequest(AbjHelpModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta class."""

        verbose_name = "Solicitud de ayuda"
        verbose_name_plural = "Solicitudes de ayuda"
    
    def __str__(self):
        return self.name
