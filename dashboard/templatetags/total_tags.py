from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def total_users():
    return User.objects.all().count()

@register.simple_tag
def un_approved_members():
    return Members.objects.filter(is_active=False, Archived_Status="NOT-ARCHIVED").count()



