from django.shortcuts import render
from django.utils.translation import get_language

from seoen.models import HomeSeoEn
from seotr.models import HomeSeoTr

def home(request):
    template_name = 'home.html'
    home_model = HomeSeoEn if get_language() == 'en' else HomeSeoTr

    context = {
        'home': home_model.objects.all().first(),
    }
    return render(request, template_name, context)


