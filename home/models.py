from django.db import models
from django.contrib import admin
from .models import FormData

class FormDataAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2',]

admin.site.register(FormData, FormDataAdmin)
# Create your models here.
