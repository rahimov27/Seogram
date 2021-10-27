from django import template
from seo.models import Category

register = template.Library()

@register.inclusion_tag('seo/menu_tpl.html')
def show_menu(menu_class='menu'):
    category = Category.objects.all()
    return {
        'categories' : category,
        'menu_class' : menu_class,
    }