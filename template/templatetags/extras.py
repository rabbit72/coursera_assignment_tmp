from django import template

register = template.Library()


@register.filter(name="inc")
def inc(number, incr):
    return int(number) + int(incr)


@register.simple_tag
def division(first, second, to_int=False):
    first = int(first)
    second = int(second)
    if to_int:
        return first // second
    return first / second
