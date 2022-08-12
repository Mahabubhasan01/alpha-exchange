from django.urls import path
from . import views
urlpatterns = [
    path('api/users/', views.User_list),
    path('api/users/<int:pk>', views.users_detail),
    path('api/orders/', views.Order_list),
    path('api/orders/<int:pk>', views.Order_detail),
]
