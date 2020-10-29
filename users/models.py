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






# class Passport(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     corp = models.ForeignKey(Corparation, on_delete=models.SET_NULL, null=True)
#     dep = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Passport.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.passport.save()
#     print(instance.passport)