import os

from django import forms
from django.conf import settings

from kitchen_service.models import DishType


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Search by name...",
            }
        )
    )


class DishTypeForm(forms.ModelForm):
    name = forms.CharField(
        label='Title',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter name here...'
            }
        )
    )

    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'custom-file-input',
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = DishType
        fields = [
            'image',
            'name',
            'description'
        ]

    def save(self, commit=True):
        dish_type = super(
            DishTypeForm, self
        ).save(commit=False)

        if self.cleaned_data["image"]:
            image = self.cleaned_data["image"]
            file_ext = os.path.splitext(image.name)[1]

            new_image_name = f"{dish_type.name}{file_ext}"
            file_path = os.path.join(
                settings.MEDIA_ROOT,
                "types_of_dish",
                new_image_name
            )

            with open(file_path, 'wb') as new_image_file:
                for chunk in image.chunks():
                    new_image_file.write(chunk)

            dish_type.image = os.path.join(
                "types_of_dish",
                new_image_name
            )

        if commit:
            dish_type.save()

        return dish_type
