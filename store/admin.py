from django.contrib import admin

from .models import *


admin.site.site_header = "Torrenet Dev"
admin.site.site_title = "Torrenet Players"


class StoreItemAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('createDate',)
    search_fields = ('name',)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('username', 'createDate', )
    list_filter = ('createDate',)
    search_fields = ('username',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('username', 'createDate', )
    list_filter = ('createDate',)
    search_fields = ('username',)


# Register your models here.
admin.site.register(StoreItem, StoreItemAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Payment, PaymentAdmin)
