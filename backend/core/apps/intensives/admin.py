from django.contrib import admin
from core.apps.intensives.models.intensives import Intensive

@admin.register(Intensive)
class IntensiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'created_at', 'updated_at')
