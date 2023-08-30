from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, MenuCategory, Booking
from .serializers import MenuSerializer, MenuCategorySerializer
from rest_framework import generics, status
from django.contrib.auth.models import User, Group
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
def home(request):
    return render(request, 'index1.html')


#API Views
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title', 'category__name']
    filterset_fields = ['category']
    ordering_fields = ['price']


class MenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = MenuSerializer
    permission_classes=[IsAuthenticated]

