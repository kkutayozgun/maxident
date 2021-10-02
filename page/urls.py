
from django.urls import path
from page.views import (home)
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    path('', home, name='home'),

]
