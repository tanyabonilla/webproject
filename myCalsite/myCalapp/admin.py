from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Event_user)
#class EventueAdmin(admin.ModelAdmin):
#      list_display = ('title', 'description', 'get_date',)


admin.site.register(models.Event_group)
admin.site.register(models.Task_user)
admin.site.register(models.Task_group)