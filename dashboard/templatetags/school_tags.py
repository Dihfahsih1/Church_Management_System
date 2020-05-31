import markdown
from django import template
from django.utils.safestring import mark_safe
from ..models import *

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

