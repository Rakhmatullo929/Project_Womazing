from django.contrib import admin
# Register your models here.
from .models import *


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)},


admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Type),
admin.site.register(Application),
admin.site.register(Order),
admin.site.register(OrderProduct),
admin.site.register(CartItem),
