from django.contrib import admin

from .models import Player


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet Players"


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'userProfile', 'createDate', )
    list_filter = ('createDate',)
    search_fields = ('username',)


# Register your models here.
admin.site.register(Player, PlayerAdmin)
