from django.conf.urls.defaults import patterns

urlpatterns = patterns('metashare.lrquality.views',
    (r'^(?P<object_id>\w+)/report/$',
    'report'),
)