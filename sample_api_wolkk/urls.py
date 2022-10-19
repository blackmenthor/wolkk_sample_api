from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from sample_api_wolkk import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_sample.urls')),
    path('journal/', include('journals.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
