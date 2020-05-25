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
def Post_Office_Box():
    church = Church.objects.get(id=1)
    church_post_number = church.Post_Office_Box
    return church_post_number

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
def church_vision():
    church = Church.objects.get(id=1)
    vision = church.church_vision
    return vision

@register.simple_tag
def church_mission():
    church = Church.objects.get(id=1)
    mission = church.church_mission
    return mission


@register.simple_tag
def church_footer():
    church = Church.objects.get(id=1)
    church_foot = church.footer
    return church_foot

@register.simple_tag
def church_map():
    on_map = Church.objects.get(id=1)
    on_map_link = on_map.maps_embedded_link
    return on_map_link    

@register.simple_tag
def church():
    church_status = Church.objects.get(id=1)
    return church_status

@register.simple_tag
def facebook():
    fb = Church.objects.get(id=1)
    facbook = fb.facebook_url
    return facbook

@register.simple_tag
def youtube():
    yt = Church.objects.get(id=1)
    youtu = yt.youtube_url
    return youtu    