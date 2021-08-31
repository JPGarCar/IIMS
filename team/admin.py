from django.contrib import admin

from .models import Unit, Team


class PrimaryTeamInLIne(admin.TabularInline):
    model = Team
    fk_name = 'unit'
    verbose_name = 'Primary Unit'


class SecondaryTeamInLIne(admin.TabularInline):
    model = Team
    fk_name = 'secondary_unit'
    verbose_name = 'Secondary Unit'


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    inlines = [
        PrimaryTeamInLIne,
        SecondaryTeamInLIne
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
