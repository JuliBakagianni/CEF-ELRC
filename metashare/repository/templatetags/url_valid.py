from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='url_valid')
def url_valid(text):
    if not str(text).startswith("http://") and \
            not str(text).startswith("https://") and \
            not str(text).startswith("ftp://") and \
            not str(text).startswith("sftp://"):

            return "http://{}".format(text)
    else:
        return text