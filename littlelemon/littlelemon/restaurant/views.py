from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItem, User
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.template.loader import get_template


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def index(request):
        template = loader.get_template('restaurant/index.html')
        context = {}
        return HttpResponse(template.render(context, request))


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    model = Booking
    items = Booking.objects.all()
    serializer_class = BookingSerializer(items, many=True)
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        return BookingSerializer(*args, **kwargs)

    def table(request):
        response = BookingViewSet.table(request)
        return Response('list of the bookings', status=status.HTTP_200_ok)


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    model = MenuItem
    serializer_class = MenuItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SingleMenuItemView(viewsets.ViewSet):
    queryset = MenuItem.objects.all()
    model = MenuItem
    serializer_class = MenuItemSerializer

    def get(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(request, serializer.data)

    def put(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_ok, headers=headers)

    def delete(self, request, pk=None):
        item = self.get_object()
        self.perform_destroy(item)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
