from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.LoginFormView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('password-change/', views.PasswordChangeView.as_view()),
    path('logout/', views.LogoutClickView.as_view(), name='logout'),
    path('<int:page>/', views.showNext),
    path('item/<int:id>/', views.showItem),

]
