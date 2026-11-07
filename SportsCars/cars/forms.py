
from datetime import date

from django import forms

from .models import Car, CarInquiry


# ==========================================
# ADD / EDIT CAR
# ==========================================

class CarForm(forms.ModelForm):

    class Meta:
        model = Car

        fields = [
            "name",
            "brand",
            "year",
            "engine",
            "horsepower",
            "price",
            "model",
            "image",
            "description",
            "is_featured",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "e.g. Porsche 992 GT3 R",
            }),

            "brand": forms.TextInput(attrs={
                "placeholder": "e.g. Porsche",
            }),

            "year": forms.NumberInput(attrs={
                "min": 1950,
                "max": 2100,
                "placeholder": "e.g. 2024",
            }),

            "engine": forms.TextInput(attrs={
                "placeholder": "e.g. 4.2L Flat-Six",
            }),

            "horsepower": forms.NumberInput(attrs={
                "min": 1,
                "placeholder": "e.g. 565",
            }),

            "price": forms.TextInput(attrs={
                "placeholder": (
                    "e.g. 1070500 or Contact for Price"
                ),
            }),

            "model": forms.TextInput(attrs={
                "placeholder": (
                    "cars/models/2024_porsche_992_gt3_r.glb"
                ),
            }),

            "image": forms.TextInput(attrs={
                "placeholder": (
                    "cars/images/Porsche 992 GT3 R.png"
                ),
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Describe the vehicle...",
                "rows": 6,
            }),

            "is_featured": forms.CheckboxInput(),
        }

    def clean_year(self):
        year = self.cleaned_data["year"]

        if not 1950 <= year <= 2100:
            raise forms.ValidationError(
                "Enter a valid model year between 1950 and 2100."
            )

        return year

    def clean_horsepower(self):
        horsepower = self.cleaned_data["horsepower"]

        if horsepower < 1:
            raise forms.ValidationError(
                "Horsepower must be greater than zero."
            )

        return horsepower

    def clean_price(self):
        price = self.cleaned_data["price"].strip()

        if not price:
            raise forms.ValidationError(
                "Enter a price or Contact for Price."
            )

        return price

    def clean_model(self):
        model_path = self.cleaned_data["model"].strip()

        if not model_path.startswith("cars/models/"):
            raise forms.ValidationError(
                "Model path must start with cars/models/."
            )

        if not model_path.lower().endswith(".glb"):
            raise forms.ValidationError(
                "The 3D model must be a .glb file."
            )

        return model_path

    def clean_image(self):
        image_path = self.cleaned_data["image"].strip()

        if not image_path.startswith("cars/images/"):
            raise forms.ValidationError(
                "Image path must start with cars/images/."
            )

        if not image_path.lower().endswith(
            (".png", ".jpg", ".jpeg", ".webp")
        ):
            raise forms.ValidationError(
                "Use a PNG, JPG, JPEG or WEBP image."
            )

        return image_path


# ==========================================
# CAR INQUIRY
# ==========================================

class CarInquiryForm(forms.ModelForm):

    class Meta:
        model = CarInquiry

        fields = [
            "full_name",
            "email",
            "phone",
            "message",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Enter your full name",
                "autocomplete": "name",
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "Enter your email address",
                "autocomplete": "email",
            }),

            "phone": forms.TextInput(attrs={
                "placeholder": "Optional phone number",
                "autocomplete": "tel",
            }),

            "message": forms.Textarea(attrs={
                "placeholder": (
                    "Tell us what you would like "
                    "to know about this vehicle..."
                ),
                "rows": 5,
            }),
        }

    def clean_message(self):
        message = self.cleaned_data["message"].strip()

        if len(message) < 10:
            raise forms.ValidationError(
                "Please enter at least 10 characters."
            )

        return message
