from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.LoginFormView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('password-change/', views.PasswordChangeView.as_view()),
    path('logout/', views.LogoutClickView.as_view(), name='logout'),
    path('<int:page>/', views.showNext),
    path('item/<int:id>/', views.showItem),
    path('item/<int:id>/comment/', views.addComment, name='comment'),
    path('cart/', include('cart.urls')),
    path('show/', views.showItems),
    path('cabinet/', include('cabinet.urls'))
    # path('place_search/', views.pas, name='place_search'),

]
