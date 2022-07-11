from django import template
from posts.models.categorys import Category

register = template.Library()


@register.simple_tag()
def categorys():
    return Category.objects.all()
