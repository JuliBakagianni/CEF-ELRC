from django import template
from metashare.repository.mimetype_choices import MIMETYPEVALUE_TO_MIMETYPELABEL

register = template.Library()


@register.filter("mimetype_label")
def mimetype_label(input):
    mimetypes = [mimetype for mimetype in input.split(",")]
    output = []
    for m in mimetypes:
        # um = unicode(m, "utf-8")
        if m.replace(u' ', u'').lower() in MIMETYPEVALUE_TO_MIMETYPELABEL:
            output.append(MIMETYPEVALUE_TO_MIMETYPELABEL[m.replace(u' ', u'').lower()])
        else:
            output.append(m)
    return ', '.join(output)

register.tag('mime_label', mimetype_label)