from django.contrib import admin
from seoen.models import (
    KeywordsEn,
    HomeSeoEn,
    
)


SEO_FIELDS = ('seo_title', 'meta_description', 'meta_keywords')

admin.site.register(KeywordsEn)

@admin.register(HomeSeoEn)
class HomeSeoTrAdmin(admin.ModelAdmin):
    fields = ('cover_image', ) + SEO_FIELDS
