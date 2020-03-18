from django.urls import path
from . import views
urlpatterns = [
    path("", views.UserCabinet.as_view()),
]