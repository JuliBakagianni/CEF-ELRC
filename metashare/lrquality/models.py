from django.db import models
from metashare.repository.mimetype_choices import TEXTFORMATINFOTYPE_MIMETYPE_CHOICES
SOURCE_CREATOR_CHOICES = (
    ('Expert', 'Expert'),
    ('Crowd', 'Crowd'),
    ('Unknown', 'Unknown')
)

class LrQuality(models.Model):

    class Meta:
        verbose_name = "Language Resource Quality"
        verbose_name_plural = "Language Resource Qualities"
        # abstract = True
    __schema_name__ = "LRQUALITY"

    resource_name = models.CharField(max_length=1000, null=True)
    # Add a foreign key to resourceInfoType_model
    # resourceName = models.CharField

    # source_quality
    source_creator = models.CharField(max_length=1000, null=True, choices=SOURCE_CREATOR_CHOICES)
    creation_time = models.DateTimeField(null=True)
    source_document_format = models.CharField(max_length=1000, null=True, choices=TEXTFORMATINFOTYPE_MIMETYPE_CHOICES['choices'])

    #translation_quality: OneToMany

    # technical_quality
    segmentation_quality = models.CharField(max_length=1000, null=True)
    alignment_quality = models.CharField(max_length=1000, null=True)
    annotation = models.CharField(max_length=1000, null=True)

    # volume
    total = models.IntegerField(null=True)
    quality = models.IntegerField(null=True)

    # focus
    domain = models.CharField(max_length=1000, null=True)

    # legal_readiness
    ipr_cleared = models.NullBooleanField()
    anonymization_required = models.NullBooleanField()


    def get_resource(self):
        pass

    def get_resourceType(self):
        pass

    def __unicode__(self):
        return u'{0}'.format(self.resource_name)


class CorpusQuality(LrQuality):
    class Meta:
        verbose_name = "Corpus Quality"
        verbose_name_plural = "Corpus Qualities"

    extra_field = models.CharField(max_length=50, blank=True, null=True)

class Lcrquality(LrQuality):
    class Meta:
        verbose_name = "Lexical Conceptual Resource Quality"
        verbose_name_plural = "Lexical Conceptual Resource Qualities"

    extra_field = models.CharField(max_length=50, blank=True, null=True)

class LangDescquality(LrQuality):
    class Meta:
        verbose_name = "Language Description Quality"
        verbose_name_plural = "Language Description Qualities"

    extra_field = models.CharField(max_length=50, blank=True, null=True)

class TranslationQuality(models.Model):
    class Meta:
        verbose_name = "Translation Quality"
        verbose_name_plural = "Translation Qualities"

    language = models.CharField(max_length=100,)
    source = models.CharField(max_length=1000)
    document_format = models.CharField(max_length=1000)
    #text_quality
    back_to_corpusquality = models.ForeignKey(CorpusQuality, blank=True, null=True)
    back_to_lcrquality = models.ForeignKey(Lcrquality, blank=True, null=True)
    back_to_langdescquality = models.ForeignKey(LangDescquality, blank=True, null=True)

    def real_unicode_(self):
        # pylint: disable-msg=C0301
        formatargs = ['language',]
        formatstring = u'{} {}'
        return self.unicode_(formatstring, formatargs)
