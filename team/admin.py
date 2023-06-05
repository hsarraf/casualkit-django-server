from django.contrib import admin

from .models import Team


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet Team"


class TeamAdmin(admin.ModelAdmin):
    list_display = ('teamId',)
    list_filter = ('createDate',)
    search_fields = ('teamId',)


# Register your models here.
admin.site.register(Team, TeamAdmin)
