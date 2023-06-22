from django import template

register = template.Library()

@register.filter
def mongo_id(value):
    if hasattr(value, '_id'):
        return str(value._id)
    return str(value)
