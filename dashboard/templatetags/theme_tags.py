from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def active_theme():
    theme = Theme.objects.get(is_active="Yes")
    theme_name = theme.name
    return theme_name
