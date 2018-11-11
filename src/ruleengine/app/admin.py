from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Rule)
admin.site.register(models.SignalData)