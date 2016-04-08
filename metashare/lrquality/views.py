import cStringIO as StringIO
import os
import re
from cgi import escape

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.forms.models import model_to_dict

from metashare.repository.models import resourceInfoType_model, languageDescriptionInfoType_model, \
    lexicalConceptualResourceInfoType_model
from metashare.lrquality.models import LrQuality
from metashare.settings import MEDIA_ROOT, MEDIA_URL


def _render_to_pdf(template_src, context_dict, res_name):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.decode("utf-8")), dest=result, link_callback=_fetch_resources)
    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}_report.pdf"'.format(res_name)
    if not pdf.err:
        return response
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def report(request, object_id):
    lrq = _get_subclass(LrQuality.objects.get(id=object_id))
    res = resourceInfoType_model.objects.get(lr_quality=lrq)
    res_dict = {
        'type': prettify_camel_case_string(unicode(res.resourceComponentType)).split(' (')[0],
        'id': res.id
    }
    corpus_media = res.resourceComponentType.as_subclass()
    if isinstance(corpus_media, languageDescriptionInfoType_model):
            res_dict['mediatype'] = [corpus_media.get_languageDescriptionType_display()]
    elif isinstance(corpus_media, lexicalConceptualResourceInfoType_model):
            res_dict['mediatype'] = [corpus_media.get_lexicalConceptualResourceType_display()]

    return _render_to_pdf(
        'lrquality/pdftemplate.html',
        {
            'pagesize': 'A4',
            'lrq': model_to_dict(lrq),
            'res': res_dict
        },
        lrq.resource_name
    )


def _fetch_resources(uri, rel):
    path = os.path.join(MEDIA_ROOT, uri.replace
    (MEDIA_URL, ""))
    return path


def _get_subclass(obj):
    subclasses = obj.__class__.__subclasses__()
    for subclass in subclasses:
        t = subclass.objects.filter(pk=obj.pk)
        if len(t) > 0: return t[0]
    return obj

def prettify_camel_case_string(cc_str):
    '''
    Prettifies the given camelCase string so that it is better readable.

    For example, "speechAnnotation-soundToTextAlignment" is converted to "Speech
    Annotation - Sound To Text Alignment". N.B.: The conversion currently only
    recognizes boundaries with ASCII letters.
    '''
    result = cc_str
    if len(result) > 1:
        # result = result.replace('-', ' - ')  AtA
        result = result.replace('_', ' ')
        result = result.replace('AtA', 'At a')
        result = re.sub(r'(\w\w)(?=[A-Z][a-z])', r'\1 ', result)
        result = ' '.join([(len(token) > 1 and (token[0].upper() + token[1:]))
                           or token[0].upper() for token in result.split()])
    return result