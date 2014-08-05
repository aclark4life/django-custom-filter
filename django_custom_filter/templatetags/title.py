from django import template


register = template.Library()


@register.filter(name='title')
def title(value):
    """
    Uppercase first letter, via http://stackoverflow.com/a/13525843
    """
    return value[0].upper() + value[1:]
