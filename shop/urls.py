from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexPage.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('logout/', views.LogoutClickView.as_view(), name='logout'),
    path('item/<int:id>/comment/', views.addComment, name='comment'),
    path('cart/', include('cart.urls')),
    path('show/', views.ItemsView.as_view()),
    path('cabinet/', include('cabinet.urls')),
    path('addToList/<int:item_id>/', views.WishListView.as_view()),
    path('search/', views.search ),
    path('comment/<int:item_id>/', views.addComment),
    path('forget/', views.ForgetPassword.as_view(), name='forget'),
    path('changePassword/<str:hash>', views.PasswordChangeView)

]
