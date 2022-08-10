from django.urls import path, include
from . import views
urlpatterns = [
    path('alluser/', views.User_list),
    path('users/<int:pk>', views.users_detail),
]
