from django import template
from ..models import *

register = template.Library()
@register.simple_tag
def all_pages():
    pages = Page.footer.all()
    return pages

