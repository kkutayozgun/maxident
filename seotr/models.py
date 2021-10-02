from django.db import models
from django.utils.translation import ugettext_lazy as _

class KeywordsTr(models.Model):
    keyword = models.CharField(_('Anahtar Kelime'), max_length=100)

    class Meta:
        verbose_name = _('TR Anahtar Kelime')
        verbose_name_plural = _('TR Anahtar Kelimeler')

    def __str__(self):
        return self.keyword


class SeoAbstractModel(models.Model):
    seo_title = models.CharField(_('SEO Başlığı:'), max_length=200, blank=True, null=True)
    meta_description = models.TextField(_('Meta Açıklaması:'), blank=True, null=True)
    meta_keywords = models.ManyToManyField(KeywordsTr, verbose_name=_('Anahtar Kelimeler'))

    class Meta:
        abstract = True


class HomeSeoTr(SeoAbstractModel):
    cover_image = models.ImageField(verbose_name=_('Kapak Görseli:'), upload_to='cover')

    class Meta:
        verbose_name = _('TR Landing Page')
        verbose_name_plural = _('TR Landing Page')

    def __str__(self):
        return self.seo_title

