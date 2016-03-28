from django import template
from os.path import dirname
from lxml import etree
from metashare.settings import ROOT_PATH

print ROOT_PATH
path = '{0}/'.format((dirname(ROOT_PATH)))
print path
xsd = etree.parse('{}misc/schema/ELRC-SHARE/META-SHARE-SimpleTypes.xsd'.format(path))
print xsd
register = template.Library()


@register.filter("mimetype_label")
def mimetype_label(input):
    print input
    mimetypes = [mimetype for mimetype in input.split(",")]
    output = []
    for m in mimetypes:
        print m.replace(u' ', u'').lower()
        # um = unicode(m, "utf-8")
        xpath = u"//*[@name='mimeType']/xs:simpleType/xs:restriction/xs:enumeration[@value='{}']//xs:label/text()".format(m.replace(u' ', u'').lower())
        print xpath
        output.append(''.join(xsd.xpath(xpath, namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'})))
        print output
    return ', '.join(output)

register.tag('mime_label', mimetype_label)