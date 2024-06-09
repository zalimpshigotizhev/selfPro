# Register your models here.
from django.contrib import admin

from core.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...
