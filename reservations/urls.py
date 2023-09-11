#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('menu/', MenuTableView.as_view()),
    # path('booking/', BookingTableView.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.MenuItemSingleView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('users/', views.UserView.as_view()),
    path('users/<int:pk>', views.UserSingleView.as_view()),
    
]