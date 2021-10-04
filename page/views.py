from django.shortcuts import render, redirect
from django.utils.translation import get_language
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


from seoen.models import HomeSeoEn
from seotr.models import HomeSeoTr

def home(request):
    template_name = 'home.html'
    home_model = HomeSeoEn if get_language() == 'en' else HomeSeoTr

    context = {
        'home': home_model.objects.all().first(),
    }
    return render(request, template_name, context)


def handle_contact_form(request):
    sender = settings.DEFAULT_FROM_EMAIL
    receivers = settings.CONTACT_FORM_RECEIVER
    if request.method == 'POST':
        try:
            firstname = request.POST.get('firstName', default="")
            lastname = request.POST.get('lastName', default="")
            treatmentchoice = request.POST.get('treatmentchoice', default="")
            email = request.POST.get('email', default="")
            phone = request.POST.get('phone', default="")
            contactmethod = request.POST.get('contactmethod', default="")
            message = request.POST.get('message', default="")
            redirectkey = request.POST.get('redirectkey')

            email_template = get_template('emailtemps/contact_email_template.html')
            subject = f"Webozel Maxident {firstname} {lastname} tarafından mesaj alındı"

            context = {
                'firstname': firstname,
                'lastname': lastname,
                'treatmentchoice': treatmentchoice,
                'email': email,
                'phone': phone,
                'contactmethod': contactmethod,
                'message': message,
            }
            content = email_template.render(context)
            msg = EmailMultiAlternatives(subject, message, sender, receivers)
            msg.attach_alternative(content, 'text/html')
            msg.send()
        except Exception as e:
            print(e)
            messages.error(request, _("Mesajınızı gönderirken hata oluştu!."))
        else:
            messages.success(request, _("Mesajınız başarıyla iletildi! En kısa süre içerisinde geri dönüş sağlayacağız."))
        
    return redirect(request.META['HTTP_REFERER'] + redirectkey)