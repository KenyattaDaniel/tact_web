from django.contrib import admin

from .models import Tactic

class TacticAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','created','modified')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Tactic, TacticAdmin)