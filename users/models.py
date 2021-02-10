from django.db import models
from django.contrib.auth.models import User
from structure.models import Corparation, Department
# from django.dispatch import receiver
# from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserP(AbstractUser):
    corp = models.ForeignKey(Corparation, on_delete=models.SET_NULL, null=True)
    dep = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

