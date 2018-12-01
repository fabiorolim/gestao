from django.contrib import admin
from django.urls import path
from .views import ola, list, new, update, delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ola/', ola, name='ola'),
    path('list/', list, name='person_list'),
    path('new/', new, name='person_new'),
    path('update/<int:id>', update, name='person_update'),
    path('delete/<int:id>', delete, name='person_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
