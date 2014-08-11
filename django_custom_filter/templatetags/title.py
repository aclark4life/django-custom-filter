from django import template


register = template.Library()


@register.filter(name='custom_title')
def custom_title(value):
    """
    Uppercase first letter, via http://stackoverflow.com/a/13525843
    """
    return value[0].upper() + value[1:]
