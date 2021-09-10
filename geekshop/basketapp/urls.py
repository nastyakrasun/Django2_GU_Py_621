from django.urls import path
import basketapp.views as basket_views

app_name = 'basketapp'

urlpatterns = [
    path('', basket_views.basket, name='basket'),
    path('add/<int:pk>/', basket_views.basket_add, name='add'),
    path('remove/<int:pk>/', basket_views.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket_views.basket_edit, name='edit'),
]
