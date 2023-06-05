from django.contrib import admin

from .models import UserProfile


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet User Profile"


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'emailAddress', 'gender', 'displayName',)
    list_filter = ('createDate',)
    search_fields = ('username', 'emailAddress', 'gender',)


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
