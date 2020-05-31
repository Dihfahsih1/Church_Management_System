from django import template

register = template.Library()


@register.simple_tag()
def multiply(fee_amount, student_discount, *args, **kwargs):
    net_discount = fee_amount * student_discount
    return net_discount


@register.simple_tag()
def subtract(total_amount, student_discount, *args, **kwargs):
    net_amount = total_amount - student_discount
    return net_amount
