from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserP

class CustomcreateuserForm(UserCreationForm):
    class Meta:
        model = UserP
        fields = '__all__'