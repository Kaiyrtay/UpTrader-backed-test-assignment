# menu_tags.py
from django import template
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    menu_items = MenuItem.objects.filter(parent=None)

    def render_menu_items(menu_items):
        result = ''
        for item in menu_items:
            active = 'active' if current_path == item.url else ''
            children = item.children.all()
            result += f'<li class="{active}"><a href="{item.url}">{item.title}</a>'
            if children:
                result += '<ul>'
                result += render_menu_items(children)
                result += '</ul>'
            result += '</li>'
        return result

    if menu_items:
        menu_html = render_menu_items(menu_items)
        return mark_safe(menu_html)

    return mark_safe('No menu items available. Go to <a href="/admin">Admin panel</a>')
