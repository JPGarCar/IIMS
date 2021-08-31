from django.contrib import admin

from .models import Official


@admin.register(Official)
class OfficialAdmin(admin.ModelAdmin):
    pass
