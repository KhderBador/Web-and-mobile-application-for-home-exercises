from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("",include("course.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=[re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]

