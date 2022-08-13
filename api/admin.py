from django.contrib import admin

from api.models import Blog, Order, Review

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "name",
                    "email",
                    "send_method",
                    "receive_method",
                    "send_amount",
                    "receive_amount",
                    "send_number",
                    "receive_number",
                    "contact_number"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'info', 'img', 'date']


@admin.register(Review)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'info', 'img', 'date']
