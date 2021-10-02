from django.contrib import admin
from seotr.models import (
    KeywordsTr,
    HomeSeoTr,
    
)


SEO_FIELDS = ('seo_title', 'meta_description', 'meta_keywords')

admin.site.site_header = 'Maxident'

admin.site.register(KeywordsTr)


@admin.register(HomeSeoTr)
class HomeSeoTrAdmin(admin.ModelAdmin):
    fields = ('cover_image', ) + SEO_FIELDS
