
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    path(settings.ADMIN_URL, admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += i18n_patterns(
    path('', include('page.urls')),
)
