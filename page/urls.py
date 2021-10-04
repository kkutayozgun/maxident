
from django.urls import path
from page.views import (home, handle_contact_form)
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    path('', home, name='home'),
    path('sendmessage', handle_contact_form, name='sendmessage'),

]
