from django import template

register = template.Library()

@register.filter(name='title')
def title():
    """
    """
