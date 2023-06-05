from django.contrib import admin

from .models import Score


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet Players"


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('username', 'level', 'createDate', )
    list_filter = ('createDate',)
    search_fields = ('username',)


# Register your models here.
admin.site.register(Score, ScoreAdmin)
