from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def phone_number():
    church = Church.objects.get(id=1)
    church_phone_number = church.phone
    return church_phone_number


@register.simple_tag
def email_address():
    church = Church.objects.get(id=1)
    church_email_address = church.email_address
    return church_email_address


@register.simple_tag
def fax():
    church = Church.objects.get(id=1)
    church_fax_number = church.fax
    return church_fax_number


@register.simple_tag
def church_address():
    church = Church.objects.get(id=1)
    church_area_address = church.address
    return church_area_address


@register.simple_tag
def church_latitude():
    church = Church.objects.get(id=1)
    church_area_latitude = church.latitude
    return church_area_latitude


@register.simple_tag
def church_longitude():
    church = Church.objects.get(id=1)
    church_area_longitude = church.longitude
    return church_area_longitude


@register.simple_tag
def church_name():
    church = Church.objects.get(id=1)
    church_full_name = church.church_name
    return church_full_name

@register.simple_tag
def church_footer():
    church = Church.objects.get(id=1)
    church_foot = church.footer
    return church_foot

@register.simple_tag
def church():
    church_status = Church.objects.get(id=1)
    return church_status
