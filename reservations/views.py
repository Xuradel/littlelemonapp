from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuTable, BookingTable
from .serializers import MenuTableSerializer, BookingTableSerializer, UserSerializer
from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# Using standard class base views

# class MenuTableView(APIView):
#     def get(self,request):
#         items = MenuTable.objects.all()
#         serializer = MenuTableSerializer(items, many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = MenuTableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success", "data":serializer.data})
        
# class BookingTableView(APIView):
#     def get(self,request):
#         items = BookingTable.objects.all()
#         serializer = BookingTableSerializer(items, many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = BookingTableSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success", "data":serializer.data})

# Using generic views

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class MenuItemSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
    permission_classes = [IsAuthenticated]