from django.contrib import admin

from core.apps.intensives.models.intensives import Intensive
from core.apps.intensives.models.intensive_sessions import IntensiveSession


@admin.register(Intensive)
class IntensiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'created_at', 'updated_at')


@admin.register(IntensiveSession)
class IntensiveSessionAdmin(admin.ModelAdmin):
    ...
