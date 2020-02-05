from django import template
from ..models import *

register = template.Library()


# @register.simple_tag
# def phone_number():
#     school = School.objects.get(id=1)
#     school_phone_number = school.phone
#     return school_phone_number


# @register.simple_tag
# def email_address():
#     school = School.objects.get(id=1)
#     school_email_address = school.email_address
#     return school_email_address


# @register.simple_tag
# def fax():
#     school = School.objects.get(id=1)
#     school_fax_number = school.fax
#     return school_fax_number


# @register.simple_tag
# def school_address():
#     school = School.objects.get(id=1)
#     school_area_address = school.address
#     return school_area_address


# @register.simple_tag
# def school_latitude():
#     school = School.objects.get(id=1)
#     school_area_latitude = school.latitude
#     return school_area_latitude


# @register.simple_tag
# def school_longitude():
#     school = School.objects.get(id=1)
#     school_area_longitude = school.longitude
#     return school_area_longitude


# @register.simple_tag
# def school_name():
#     school = School.objects.get(id=1)
#     school_full_name = school.school_name
#     return school_full_name


# @register.simple_tag
# def school():
#     school_status = School.objects.get(id=1)
#     return school_status
