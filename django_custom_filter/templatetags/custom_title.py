from django import template


register = template.Library()


@register.filter(name='custom_title')
def custom_title(value):
    """
    Uppercase first letter of each word leaving remaining characters
    unchanged.
    """
    return ' '.join([word[0].capitalize() + word[1:] for word in value.split()])
