from django import template
from ..models import *
from ..views import *

register = template.Library()
@register.simple_tag
def user_access(request):
    return (request.user.Role == 'Secretary' or 'Admin' or 'SuperAdmin' or 'Assistant_Admin')

