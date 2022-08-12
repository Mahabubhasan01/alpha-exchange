from django.contrib import admin

from api.models import Order

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
                    "contact_number" ]
