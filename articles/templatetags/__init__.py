from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="strong")
@stringfilter
def strong(value):
    return "<strong>" + value + "</strong>"
