from django.contrib import admin
from .models import Car, CarInquiry

# Register your models here.

# ==========================================
# CAR ADMIN
# ==========================================

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "brand",
        "year",
        "horsepower",
        "price",
        "is_featured",
    )

    list_filter = (
        "brand",
        "year",
        "is_featured",
    )

    search_fields = (
        "name",
        "brand",
        "engine",
    )

    list_editable = (
        "is_featured",
    )


# ==========================================
# CAR INQUIRY ADMIN
# ==========================================

@admin.register(CarInquiry)
class CarInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "car",
        "email",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
        "car",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "car__name",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
    )

    list_select_related = (
        "car",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (
        (
            "Vehicle",
            {
                "fields": ("car",)
            }
        ),

        (
            "Customer Information",
            {
                "fields": (
                    "full_name",
                    "email",
                    "phone",
                )
            }
        ),

        (
            "Inquiry Details",
            {
                "fields": (
                    "message",
                    "status",
                    "created_at",
                )
            }
        ),
    )
