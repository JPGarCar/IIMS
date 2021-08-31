from django.contrib import admin

from league.models import Gender, Pool, Tier, Term, Location, Activity, Week, Day


class PoolInLine(admin.TabularInline):
    model = Pool
    extra = 0
    show_change_link = True
    show_full_result_count = True

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class WeekInLine(admin.TabularInline):
    model = Week
    extra = 0


class DayInLine(admin.TabularInline):
    model = Day
    extra = 0


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    inlines = [
        PoolInLine,
    ]


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    inlines = [
        PoolInLine,
    ]


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    inlines = [
        PoolInLine,
    ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [
        PoolInLine,
    ]


@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    inlines = [
        WeekInLine,
    ]


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    inlines = [
        DayInLine,
    ]


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    pass
