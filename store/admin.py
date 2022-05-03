from django.contrib import admin
# Register your models here.
from .models import *


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)},
