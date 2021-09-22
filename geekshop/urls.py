from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from geekshop.views import index, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('mainapp.urls', namespace='products'), name='products'),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff'), name='admin_staff'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('order/', include('ordersapp.urls', namespace='order'), name='order'),
    path('basket/', include('basketapp.urls', namespace='basket'), name='basket'),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
