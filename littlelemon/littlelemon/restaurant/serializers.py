from rest_framework import serializers
from .models import Booking, MenuItem, SingleMenuItem
from django.contrib.auth.models import User


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']


class SingleMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleMenuItem
        fields = '__all__'
