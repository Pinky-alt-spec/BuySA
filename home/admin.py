from django.contrib import admin
from home.models import * 


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']
    
    
admin.site.register(Setting, SettingAdmin)