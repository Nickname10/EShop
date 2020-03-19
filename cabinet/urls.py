from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.UserCabinet.as_view()),
    path("cart/", include('cart.urls')),
    path("remove/<int:item_id>", views.RemoveItemView.as_view()),
    path("delivered/<int:order_id>",views.OrderDeliverView.as_view()),
    path("removeWishListItem/<int:item_id>/", views.removeItem)
]