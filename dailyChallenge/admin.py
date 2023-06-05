from django.contrib import admin

from .models import *


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet Players"


class DailyChallenegAdmin(admin.ModelAdmin):
    list_display = ('username', 'nextIndex', 'createDate', )
    list_filter = ('createDate',)
    search_fields = ('username',)


# Register your models here.
admin.site.register(DailyChallenge, DailyChallenegAdmin)


class DailyChallenegContentAdmin(admin.ModelAdmin):
    list_display = ('index', 'name', )
    list_filter = ('createDate',)
    search_fields = ('index',)


# Register your models here.
admin.site.register(DailyChallenegContent, DailyChallenegContentAdmin)
