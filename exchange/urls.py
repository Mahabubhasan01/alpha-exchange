from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.Register_Form, name='register_form'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('add-blogs/', views.Add_blogs, name='add_blogs'),
    path('all-blogs/', views.All_Blogs, name='all_blogs'),
    path('blog-detail/<int:blog_id>/', views.Blog_Detail, name='blog_detail'),
    path('user-profile/', views.User_Profile, name='user_profile'),
    path('manage-user/', views.Manage_Users, name='manage_users'),
    path('manage-order/', views.Manage_Order,
         name='manage_order'),
    path('update-order/<int:pk>/', views.update_order,
         name='update_order'),
    path('transaction_history/', views.Transaction_History,
         name='transaction_history'),
    path('exchange-money/', views.Exchange_Money,
         name='exchange_money'),
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.user_logout, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),



]
