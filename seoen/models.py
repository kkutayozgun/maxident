from django.db import models
from django.utils.translation import ugettext_lazy as _

class KeywordsEn(models.Model):
    keyword = models.CharField(_('Anahtar Kelime'), max_length=100)

    class Meta:
        verbose_name = _('EN Anahtar Kelime')
        verbose_name_plural = _('EN Anahtar Kelimeler')

    def __str__(self):
        return self.keyword


class SeoAbstractModel(models.Model):
    seo_title = models.CharField(_('SEO Başlığı:'), max_length=200, blank=True, null=True)
    meta_description = models.TextField(_('Meta Açıklaması:'), blank=True, null=True)
    meta_keywords = models.ManyToManyField(KeywordsEn, verbose_name=_('Anahtar Kelimeler'))

    class Meta:
        abstract = True


class HomeSeoEn(SeoAbstractModel):
    cover_image = models.ImageField(verbose_name=_('Kapak Görseli:'), upload_to='cover')

    class Meta:
        verbose_name = _('EN Landing Page')
        verbose_name_plural = _('EN Landing Page')

    def __str__(self):
        return self.seo_title

