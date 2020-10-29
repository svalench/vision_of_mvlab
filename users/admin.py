from django.contrib import admin
from users.models import UserP
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomcreateuserForm

class CustomAdmin(UserAdmin):
    model = UserP
    add_form = CustomcreateuserForm


admin.site.register(UserP, CustomAdmin)
