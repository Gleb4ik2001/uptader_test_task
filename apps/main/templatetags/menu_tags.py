from django import template
from main.models import Menu 

register = template.Library()

@register.simple_tag()
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(title=menu_name)
    except Menu.DoesNotExist:
        menu = None

    return {
        'menu': menu
    }