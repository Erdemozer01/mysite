from django import template
from blog.models.title import Titles

register = template.Library()


@register.simple_tag()
def title():
    return Titles.objects.all()
