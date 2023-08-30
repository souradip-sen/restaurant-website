from django.urls import path
from . import views
#from .views import MenuItemView, MenuView

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.MenuView.as_view(), name='menu'),
    path('menu/<int:pk>', views.MenuItemView.as_view(), name='menu-item'),
    path('booking',views.BookingView.as_view(), name='booking'),
    
    
]