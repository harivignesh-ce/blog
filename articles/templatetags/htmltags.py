from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="strong", needs_autoescape=False)
@stringfilter
def strong(value):
    return mark_safe("<strong>" + value + "</strong>")
