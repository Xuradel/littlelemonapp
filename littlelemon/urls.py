#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from reservations import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('reservations.urls')),
   path('restaurant/booking/', include(router.urls)),
   path('api-auth/', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
]