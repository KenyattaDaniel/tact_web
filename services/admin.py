from django.contrib import admin

from .models import Service, Offering

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','owner','created','modified')
    list_filter = ('created','modified','owner')
    search_fields = ('title','owner')
    raw_id_fields = ('owner',)
    date_hierarchy = 'modified'
    ordering = ['modified', 'created']


class OfferingAdmin(admin.ModelAdmin):
    list_display = ('title','service', 'owner','created','modified')
    list_filter = ('service','created','modified','owner')
    search_fields = ('title','service','owner', 'service')
    raw_id_fields = ('owner',)
    date_hierarchy = 'modified'
    ordering = ['modified', 'created']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Offering, OfferingAdmin)
