from django import template
register = template.Library()
i = 0
@register.filter(name='qwer')
def qwer(value):
    global i
    if i < len(value):
        value = value[i]
        i = i+1
        return str(value)
    else:
        return "0"
