from django import forms

from hobbie.models import Hobbie

class HobbieForm(forms.ModelForm):
    name = forms.CharField(
        label="Pasatiempo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "hobbie-name",
                "placeholder": "Pasatiempo",
                "required": "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripción",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "hobbie-description",
                "placeholder": "Descripción",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "hobbie-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Hobbie
        fields = ["name", "description", "email"]
