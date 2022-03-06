"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include
# Tiene la configuración de los media url
from django.conf import settings
# En caso de qué no esté subido, generemos a partir de un archivo static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')), 
    re_path('', include('applications.entrada.urls')), 
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)