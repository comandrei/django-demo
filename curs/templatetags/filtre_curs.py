from django import template

register = template.Library()

@register.filter
def my_title(value, arg):
    return str(value).upper() + "test" + arg

@register.simple_tag
def my_tag():
    return "foo"