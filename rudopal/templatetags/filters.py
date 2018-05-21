from django import template

register = template.Library()

@register.filter(is_safe=True)
    def modulo(num, val):
        return num % val