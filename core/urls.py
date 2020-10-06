from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import medicos_list, medicos_create, medicos_update, medicos_delete

urlpatterns = [
    path('', medicos_list, name='medicos_list'),
    path('create', medicos_create, name='medicos_create'),
    path('update/<int:pk>/', medicos_update, name='medicos_update'),
    path('delete/<int:pk>/', medicos_delete, name='medicos_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()