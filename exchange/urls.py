from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('register', views.Register_Form, name='register_form'),
]
