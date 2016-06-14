from django.conf.urls.defaults import patterns, url
from haystack.views import search_view_factory
from haystack.query import SearchQuerySet

from metashare.repository.forms import FacetedBrowseForm
from metashare.repository.views import MetashareFacetedSearchView

def get_SearchQuerySet():
  sqs = SearchQuerySet() \
    .facet("languageNameFilter") \
    .facet("languageScriptFilter") \
    .facet("languageRegionFilter") \
    .facet("languageVariantFilter") \
    .facet("resourceTypeFilter") \
    .facet("availabilityFilter") \
    .facet("licenceFilter") \
    .facet("restrictionsOfUseFilter") \
    .facet("lingualityTypeFilter") \
    .facet("multilingualityTypeFilter") \
    .facet("mimeTypeFilter") \
    .facet("bestPracticesFilter") \
    .facet("domainFilter") \
    .facet("corpusAnnotationTypeFilter") \
    .facet("corpusAnnotationFormatFilter") \
    .facet("languageDescriptionLDTypeFilter") \
    .facet("languageDescriptionEncodingLevelFilter") \
    .facet("lexicalConceptualResourceLRTypeFilter") \
    .facet("lexicalConceptualResourceEncodingLevelFilter") \
    .facet("lexicalConceptualResourceLinguisticInformationFilter") \
    .facet("textTextGenreFilter") \
    .facet("textTextTypeFilter") \
    .facet("languageVarietyFilter") \
    .facet("appropriatenessForDSIFilter") \
    .facet("publicationStatusFilter")
  return sqs


urlpatterns = patterns('metashare.repository.views',
  (r'^browse/(?P<resource_name>[\w\-]*)/(?P<object_id>\w+)/$',
    'view'),
  (r'^browse/(?P<object_id>\w+)/$',
    'view'),
  (r'^download/(?P<object_id>\w+)/$',
    'download'),
  (r'^download_contact/(?P<object_id>\w+)/$',
    'download_contact'),
  url(r'^search/$',search_view_factory(view_class=MetashareFacetedSearchView,
                        form_class=FacetedBrowseForm,
                        template='repository/search.html',
                        searchqueryset=get_SearchQuerySet())),
  url(r'simple_form', 'simple_form'),
  url(r'contributions','manage_contributed_data'),
  (r'addtodb/$', 'addtodb'),
  url(r'repo_report', 'repo_report'),
)
