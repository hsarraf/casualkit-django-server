from django.contrib import admin

from .models import Social


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet Social"


class SocialAdmin(admin.ModelAdmin):
    list_display = ('username', 'socialId',)
    list_filter = ('createDate',)
    search_fields = ('username',)


# Register your models here.
admin.site.register(Social, SocialAdmin)
