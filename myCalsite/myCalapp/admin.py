from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Event_user)
admin.site.register(models.Event_group)
admin.site.register(models.Task_user)
admin.site.register(models.Task_group)