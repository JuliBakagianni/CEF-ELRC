from django.contrib import admin
from django import forms
from metashare import settings
from metashare.repository.editor.superadmin import SchemaModelAdmin
from metashare.repository.editor.inlines import SchemaModelInline

from metashare.repository.models import documentUnstructuredString_model
admin.site.register(documentUnstructuredString_model)


from metashare.repository.models import \
    actorInfoType_model, \
    annotationInfoType_model, \
    characterEncodingInfoType_model, \
    communicationInfoType_model, \
    corpusInfoType_model, \
    corpusMediaTypeType_model, \
    corpusTextInfoType_model, \
    distributionInfoType_model, \
    documentInfoType_model, \
    documentListType_model, \
    documentationInfoType_model, \
    domainInfoType_model, \
    languageDescriptionEncodingInfoType_model, \
    languageDescriptionInfoType_model, \
    languageDescriptionMediaTypeType_model, \
    languageDescriptionTextInfoType_model, \
    languageInfoType_model, \
    lexicalConceptualResourceEncodingInfoType_model, \
    lexicalConceptualResourceInfoType_model, \
    lexicalConceptualResourceMediaTypeType_model, \
    lexicalConceptualResourceTextInfoType_model, \
    licenceInfoType_model, \
    lingualityInfoType_model, \
    metadataInfoType_model, \
    organizationInfoType_model, \
    organizationListType_model, \
    personInfoType_model, \
    personListType_model, \
    projectListType_model, \
    resourceComponentTypeType_model, \
    resourceDocumentationInfoType_model, \
    resourceInfoType_model, \
    sizeInfoType_model, \
    targetResourceInfoType_model, \
    textClassificationInfoType_model, \
    textFormatInfoType_model, \
    identificationInfoType_model, \
    languageVarietyInfoType_model, \
    resourceCreationInfoType_model, \
    creationInfoType_model, \
    projectInfoType_model


# pylint: disable-msg=C0103
class annotationInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = annotationInfoType_model
    collapse = True
    fk_name = 'back_to_corpustextinfotype_model'
# pylint: disable-msg=C0103
class characterEncodingInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = characterEncodingInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_corpustextinfotype_model'


# pylint: disable-msg=C0103
class characterEncodingInfo_model_inline_languageDescriptionTextInfoType_model(SchemaModelInline):
    model = characterEncodingInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_languagedescriptiontextinfotype_model'


# pylint: disable-msg=C0103
class characterEncodingInfo_model_inline_lexicalConceptualResourceTextInfoType_model(SchemaModelInline):
    model = characterEncodingInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_lexicalconceptualresourcetextinfotype_model'


# pylint: disable-msg=C0103
class corpusInfo_model_inline(SchemaModelInline):
    model = corpusInfoType_model


# pylint: disable-msg=C0103
class corpusTextInfo_model_inline(SchemaModelInline):
    model = corpusTextInfoType_model
    collapse = True

# pylint: disable-msg=C0103
class documentInfo_model_inline(SchemaModelInline):
    model = documentInfoType_model


# pylint: disable-msg=C0103
class domainInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = domainInfoType_model
    template = 'admin/edit_inline/stacked.html'
    fk_name = 'back_to_corpustextinfotype_model'

# pylint: disable-msg=C0103
class domainInfo_model_inline_languageDescriptionTextInfoType_model(SchemaModelInline):
    model = domainInfoType_model
    template = 'admin/edit_inline/stacked.html'
    fk_name = 'back_to_languagedescriptiontextinfotype_model'


# pylint: disable-msg=C0103
class domainInfo_model_inline_lexicalConceptualResourceTextInfoType_model(SchemaModelInline):
    model = domainInfoType_model
    template = 'admin/edit_inline/stacked.html'
    fk_name = 'back_to_lexicalconceptualresourcetextinfotype_model'

# pylint: disable-msg=C0103
class languageDescriptionInfo_model_inline(SchemaModelInline):
    model = languageDescriptionInfoType_model



# pylint: disable-msg=C0103
class languageInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = languageInfoType_model
    fk_name = 'back_to_corpustextinfotype_model'

# pylint: disable-msg=C0103
class languageInfo_model_inline_languageDescriptionTextInfoType_model(SchemaModelInline):
    model = languageInfoType_model
    fk_name = 'back_to_languagedescriptiontextinfotype_model'



# pylint: disable-msg=C0103
class languageInfo_model_inline_lexicalConceptualResourceTextInfoType_model(SchemaModelInline):
    model = languageInfoType_model
    fk_name = 'back_to_lexicalconceptualresourcetextinfotype_model'


# pylint: disable-msg=C0103
class lexicalConceptualResourceInfo_model_inline(SchemaModelInline):
    model = lexicalConceptualResourceInfoType_model


# pylint: disable-msg=C0103
class licenceInfo_model_inline(SchemaModelInline):
    model = licenceInfoType_model
    class Media:
        js = (settings.ADMIN_MEDIA_PREFIX + '/js/showHideFields.js',)
    # collapse = True


# pylint: disable-msg=C0103
class organizationInfo_model_inline(SchemaModelInline):
    model = organizationInfoType_model


# pylint: disable-msg=C0103
class personInfo_model_inline(SchemaModelInline):
    model = personInfoType_model


# pylint: disable-msg=C0103
class sizeInfo_model_inline_languageInfoType_model(SchemaModelInline):
    model = sizeInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_languageinfotype_model'


# pylint: disable-msg=C0103
class sizeInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = sizeInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_corpustextinfotype_model'



# pylint: disable-msg=C0103
class sizeInfo_model_inline_languageDescriptionTextInfoType_model(SchemaModelInline):
    model = sizeInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_languagedescriptiontextinfotype_model'


# pylint: disable-msg=C0103
class sizeInfo_model_inline_lexicalConceptualResourceTextInfoType_model(SchemaModelInline):
    model = sizeInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_lexicalconceptualresourcetextinfotype_model'



# pylint: disable-msg=C0103
class textClassificationInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = textClassificationInfoType_model
    collapse = False
    fk_name = 'back_to_corpustextinfotype_model'


# pylint: disable-msg=C0103
class textFormatInfo_model_inline_corpusTextInfoType_model(SchemaModelInline):
    model = textFormatInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_corpustextinfotype_model'



# pylint: disable-msg=C0103
class textFormatInfo_model_inline_languageDescriptionTextInfoType_model(SchemaModelInline):
    model = textFormatInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_languagedescriptiontextinfotype_model'


# pylint: disable-msg=C0103
class textFormatInfo_model_inline_lexicalConceptualResourceTextInfoType_model(SchemaModelInline):
    model = textFormatInfoType_model
    template = 'admin/edit_inline/tabular.html'
    fk_name = 'back_to_lexicalconceptualresourcetextinfotype_model'

admin.site.register(actorInfoType_model, SchemaModelAdmin)
admin.site.register(annotationInfoType_model, SchemaModelAdmin)
admin.site.register(characterEncodingInfoType_model, SchemaModelAdmin)
admin.site.register(communicationInfoType_model, SchemaModelAdmin)
admin.site.register(corpusInfoType_model, SchemaModelAdmin)
admin.site.register(corpusMediaTypeType_model, SchemaModelAdmin)
admin.site.register(corpusTextInfoType_model, SchemaModelAdmin)
admin.site.register(creationInfoType_model, SchemaModelAdmin)
admin.site.register(distributionInfoType_model, SchemaModelAdmin)
admin.site.register(documentInfoType_model, SchemaModelAdmin)
admin.site.register(documentListType_model, SchemaModelAdmin)
admin.site.register(documentationInfoType_model, SchemaModelAdmin)
admin.site.register(domainInfoType_model, SchemaModelAdmin)
admin.site.register(identificationInfoType_model, SchemaModelAdmin)
admin.site.register(languageDescriptionEncodingInfoType_model, SchemaModelAdmin)
admin.site.register(languageDescriptionInfoType_model, SchemaModelAdmin)
admin.site.register(languageDescriptionMediaTypeType_model, SchemaModelAdmin)
admin.site.register(languageDescriptionTextInfoType_model, SchemaModelAdmin)
admin.site.register(languageInfoType_model, SchemaModelAdmin)
admin.site.register(languageVarietyInfoType_model, SchemaModelAdmin)
admin.site.register(lexicalConceptualResourceEncodingInfoType_model, SchemaModelAdmin)
admin.site.register(lexicalConceptualResourceInfoType_model, SchemaModelAdmin)
admin.site.register(lexicalConceptualResourceMediaTypeType_model, SchemaModelAdmin)
admin.site.register(lexicalConceptualResourceTextInfoType_model, SchemaModelAdmin)
admin.site.register(licenceInfoType_model, SchemaModelAdmin)
admin.site.register(lingualityInfoType_model, SchemaModelAdmin)
admin.site.register(metadataInfoType_model, SchemaModelAdmin)
admin.site.register(organizationInfoType_model, SchemaModelAdmin)
admin.site.register(organizationListType_model, SchemaModelAdmin)
admin.site.register(personInfoType_model, SchemaModelAdmin)
admin.site.register(personListType_model, SchemaModelAdmin)
admin.site.register(projectInfoType_model, SchemaModelAdmin)
admin.site.register(projectListType_model, SchemaModelAdmin)
admin.site.register(resourceComponentTypeType_model, SchemaModelAdmin)
admin.site.register(resourceCreationInfoType_model, SchemaModelAdmin)
admin.site.register(resourceDocumentationInfoType_model, SchemaModelAdmin)
admin.site.register(resourceInfoType_model, SchemaModelAdmin)
admin.site.register(sizeInfoType_model, SchemaModelAdmin)
admin.site.register(targetResourceInfoType_model, SchemaModelAdmin)
admin.site.register(textClassificationInfoType_model, SchemaModelAdmin)
admin.site.register(textFormatInfoType_model, SchemaModelAdmin)
from metashare.repository.editor import manual_admin_registration
manual_admin_registration.register()

