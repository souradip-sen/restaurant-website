from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('menu-category', views.MenuCategoryView.as_view(), name='menu-category'),
    path('menu', views.MenuView.as_view(), name='menu'),
    path('menu/<int:pk>', views.MenuItemView.as_view(), name='menu-item'),
    path('booking',views.BookingView.as_view(), name='booking'),
    path('api-token-auth', obtain_auth_token),
    
]