from django import template

register = template.Library()

@register.filter(name='get_by_key')
def get_by_key(dictionary, key):
    return dictionary.get(key)
