from rest_framework import serializers
from .models import MenuTable, BookingTable
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','password']
        # extra_kwargs = {
        #     'password': {'write_only': True}  # Ensure the password field is write-only
        # }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Remove the password field from validated_data
        user = User(**validated_data)
        user.set_password(password)  # Use set_password to securely hash the password
        user.save()
        return user
    
    
class MenuTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = "__all__"
        
class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = "__all__"
        
