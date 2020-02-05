from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def total_users():
    return User.objects.all().count()


@register.simple_tag
def total_students():
    return Members.objects.all().count()


@register.simple_tag
def total_guardians():
    return Visitors.objects.all().count()


@register.simple_tag
def total_employees():
    return StaffDetails.objects.all().count()



