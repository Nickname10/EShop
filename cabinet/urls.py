from django.urls import path
from . import views
urlpatterns = [
    path("", views.UserCabinet.as_view()),
    path("remove/<int:item_id>", views.RemoveItemView.as_view()),
    path("delivered/<int:order_id>",views.OrderDeliverView.as_view()),

]