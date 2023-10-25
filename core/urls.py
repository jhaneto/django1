
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, contato, produto


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato),
    path('produto/<int:pk>', produto, name='produto'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)