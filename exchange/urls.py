from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('register', views.Register_Form, name='register_form'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('add-blogs/', views.Add_blogs, name='add_blogs'),
    path('user-profile/', views.User_Profile, name='user_profile'),
    path('manage-user/', views.Manage_Users, name='manage_users'),
    path('transaction_history/', views.Transaction_History,
         name='transaction_history'),
    path('logout/', views.user_logout, name='logout'),

]
