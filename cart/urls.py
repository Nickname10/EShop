from django.urls import path

from . import views

urlpatterns = [
    # path('', views.cart_detail, name='cart-detail'),
    path('add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('view/', views.cart_view, name='cart_view')

]
