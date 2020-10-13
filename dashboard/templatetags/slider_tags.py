from django import template
from ..models import *

register = template.Library()

@register.simple_tag
def sliding_image1():
    try:
        detail = Slider.objects.get(id=1)
        image = detail.slider_image.url
        return image
    except:
        pass

@register.simple_tag
def sliding_image2():
    try:
        detail = Slider.objects.get(id=2)
        image = detail.slider_image.url
        return image 
    except:
        pass 
 
@register.simple_tag
def sliding_image3():
    try:
        detail = Slider.objects.get(id=3)
        image = detail.slider_image.url
        return image
    except:
        pass

