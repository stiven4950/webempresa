from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    # core URLs
    path('', include('core.urls')),
    # services URLs
    path('', include('services.urls')),
    # blog URLs
    path('blog/', include('blog.urls')),
    # pages URLs
    path('pages/', include('pages.urls')),
    # contact URLs
    path('contact/', include('contact.urls')),
    # admin URLs
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
