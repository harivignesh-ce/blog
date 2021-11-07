""" from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


def user_is_author(request):
    return request.user. """
