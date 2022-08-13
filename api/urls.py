from django.urls import path
from . import views
urlpatterns = [
    path('api/users/', views.User_list),
    path('api/users/<int:pk>', views.users_detail),
    path('api/orders/', views.Order_list),
    path('api/orders/<int:pk>', views.Order_detail),
    path('api/blogs/', views.Blog_list),
    path('api/blogs/<int:pk>', views.Blog_detail),
    path('api/reviews/', views.Review_list),
    path('api/reviews/<int:pk>', views.Review_detail),
]
