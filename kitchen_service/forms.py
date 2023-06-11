from django import forms


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
