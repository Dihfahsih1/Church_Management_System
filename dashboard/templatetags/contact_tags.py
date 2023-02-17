from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def phone_number():
    try:
        church = Church.objects.get(id=1)
        church_phone_number = church.phone
        return church_phone_number
    except:
        pass


@register.simple_tag
def email_address():
    try:
        church = Church.objects.get(id=1)
        church_email_address = church.email_address
        return church_email_address
    except:
        pass   
@register.simple_tag
def Post_Office_Box():
    try:
        church = Church.objects.get(id=1)
        church_post_number = church.Post_Office_Box
        return church_post_number
    except:
        pass   

@register.simple_tag
def church_address():
    try:
        church = Church.objects.get(id=1)
        church_area_address = church.address
        return church_area_address
    except:
        pass   

@register.simple_tag
def church_latitude():
    try:
        church = Church.objects.get(id=1)
        church_area_latitude = church.latitude
        return church_area_latitude
    except:
        pass   


@register.simple_tag
def church_longitude():
    try:
        church = Church.objects.get(id=1)
        church_area_longitude = church.longitude
        return church_area_longitude
    except:
        pass   

@register.simple_tag
def church_name():
    try:
        church = Church.objects.get(id=1)
        church_full_name = church.church_name
        return church_full_name
    except:
        pass   
@register.simple_tag
def church_vision():
    try:
        church = Church.objects.get(id=1)
        vision = church.church_vision
        return vision
    except:
        pass   
@register.simple_tag
def church_mission():
    try:
        church = Church.objects.get(id=1)
        mission = church.church_mission
        return mission
    except:
        pass  

@register.simple_tag
def church_footer():
    try:
        church = Church.objects.get(id=1)
        church_foot = church.footer
        return church_foot
    except:
        pass   
@register.simple_tag
def church_map():
    try:
        on_map = Church.objects.get(id=1)
        on_map_link = on_map.maps_embedded_link
        return on_map_link 
    except:
        pass   

@register.simple_tag
def church():
    try:
        church_status = Church.objects.get(id=1)
        return church_status
    except:
        pass   
@register.simple_tag
def facebook():
    try:
        fb = Church.objects.get(id=1)
        facbook = fb.facebook_url
        return facbook
    except:
        pass   

@register.simple_tag
def youtube():
    try:
        yt = Church.objects.get(id=1)
        youtu = yt.youtube_url
        return youtu
    except:
        pass   