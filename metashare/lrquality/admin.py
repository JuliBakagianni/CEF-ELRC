from django.contrib import admin
from metashare.lrquality.models import LrQuality, TranslationQuality, CorpusQuality, LangDescquality, Lcrquality


class TranslationQualityAdmin_CorpusQuality(admin.StackedInline):
    model = TranslationQuality
    readonly_fields = ('language',)
    fieldsets = (
        ('Languages', {
            'fields': ('language', 'source',)
        }),

        ('Document Format', {
            'fields': ('document_format',)
        }),
    )
    extra = 1
    # template = 'admin/edit_inline/stacked.html'
    fk_name = 'back_to_corpusquality'

class TranslationQualityAdmin_LCRQuality(admin.StackedInline):
    model = TranslationQuality
    readonly_fields = ('language',)
    fieldsets = (
        ('Languages', {
            'fields': ('language', 'source',)
        }),

        ('Document Format', {
            'fields': ('document_format',)
        }),
    )
    extra = 1
    # template = 'admin/edit_inline/stacked.html'
    fk_name = 'back_to_lcrquality'


class TranslationQualityAdmin_LangDescQuality(admin.StackedInline):
    model = TranslationQuality
    readonly_fields = ('language',)
    fieldsets = (
        ('Languages', {
            'fields': ('language', 'source',)
        }),

        ('Document Format', {
            'fields': ('document_format',)
        }),
    )
    extra = 1
    # template = 'admin/edit_inline/stacked.html'
    fk_name = 'back_to_langdescquality'

class LrQualityAdmin(admin.ModelAdmin):
    """
    Model admin class for language resource quality instances.
    """


    readonly_fields = ('resource_name',)
    fieldsets = (
        ('ID',{
            'fields': ('resource_name',)
        }),
        ('Source Quality', {
            'fields': ('source_creator', 'creation_time', 'source_document_format')
        }),

        ('Technical Quality', {
            'fields': ('segmentation_quality', 'alignment_quality', 'annotation')
        }),

        ('Volume', {
            'fields': ('total', 'quality' )
        }),

        ('Focus', {
            'fields': ('domain',)
        }),

        ('Legal Readiness', {
            'fields': ('ipr_cleared', 'anonymization_required')
        }),
    )

class CorpusQualityAdmin(LrQualityAdmin):
    inlines = [TranslationQualityAdmin_CorpusQuality]
    fieldsets = LrQualityAdmin.fieldsets
    fieldsets += (('extra',{
            'fields': ('extra_field',)
        }),
                 )
class LangDescQualityAdmin(LrQualityAdmin):
    inlines = [TranslationQualityAdmin_LangDescQuality]
    fieldsets = LrQualityAdmin.fieldsets
    fieldsets += (('extra',{
            'fields': ('extra_field',)
        }),
                 )
class LCRQualityAdmin(LrQualityAdmin):
    inlines = [TranslationQualityAdmin_LCRQuality]
    fieldsets = LrQualityAdmin.fieldsets
    fieldsets += (('extra',{
            'fields': ('extra_field',)
        }),
                 )
# admin.site.register(LrQuality, LrQualityAdmin)
admin.site.register(CorpusQuality, CorpusQualityAdmin)
admin.site.register(LangDescquality, LangDescQualityAdmin)
admin.site.register(Lcrquality, LCRQualityAdmin)