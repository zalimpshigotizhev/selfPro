# Register your models here.
from django.contrib import admin

from core.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'phone',
        'is_active',
    ]
