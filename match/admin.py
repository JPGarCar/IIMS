from django.contrib import admin

from .models import TeamGame, Match, OfficialGame, Player


class OfficialGameInLine(admin.TabularInline):
    model = OfficialGame
    extra = 1


class PlayerInLine(admin.TabularInline):
    model = Player
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TeamGame)
class TeamGameAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInLine,
    ]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    inlines = [
        OfficialGameInLine,
    ]


@admin.register(OfficialGame)
class OfficialGameAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
