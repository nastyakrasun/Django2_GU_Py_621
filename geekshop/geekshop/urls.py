from django.contrib import admin
from django.urls import path, include
from mainapp import urls as mainapp_urls
from authapp import urls as authapp_urls
from basketapp import urls as basketapp_urls
from adminapp import urls as adminapp_urls
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_staff/', include(adminapp_urls, namespace='admin_staff'), name='admin_staff'),

    path('', views.index, name='index'),
    # path('<int:pk>', views.index, name='index'),
    # path('', views.index, name='products_all'),
    # path('', views.index, name='products_home'),
    path('contact/', views.contact, name='contact'),

    path('products/', include(mainapp_urls, namespace='products'), name='products'),
    path('basket/', include(basketapp_urls, namespace='basket'), name='basket'),
    path('auth/', include(authapp_urls, namespace='auth'), name='auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
