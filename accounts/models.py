from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=False)
    last_name = models.CharField(_('last name'), max_length=100, blank=False)
