from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('shop.html')
def categories():
    categories_list = Category.objects.all()
    return {'categories': categories_list}