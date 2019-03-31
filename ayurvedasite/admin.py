from django.contrib import admin

# Register your models here.
from .models import  Comment, Symptoms


admin.site.register(Comment)
admin.site.register(Symptoms)
