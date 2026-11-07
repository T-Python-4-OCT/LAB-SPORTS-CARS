
from decimal import Decimal, InvalidOperation

from django.db import models


# ==========================================
# CAR MODEL
# ==========================================

class Car(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    engine = models.CharField(max_length=150)
    horsepower = models.PositiveIntegerField()

    price = models.CharField(
        max_length=100,
        default="Contact for Price"
    )

    model = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    description = models.TextField()

    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} ({self.year})"

    @property
    def formatted_price(self):
        try:
            amount = Decimal(
                str(self.price).replace(",", "").strip()
            )

            if not amount.is_finite():
                return self.price

            if amount == amount.to_integral_value():
                return f"{amount:,.0f} SAR"

            return f"{amount:,.2f} SAR"

        except (InvalidOperation, ValueError):
            return self.price


# ==========================================
# CAR INQUIRY MODEL
# ==========================================

class CarInquiry(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="inquiries"
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    message = models.TextField(max_length=2000)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Car Inquiry"
        verbose_name_plural = "Car Inquiries"

    def __str__(self):
        return f"{self.full_name} - {self.car.name}"
