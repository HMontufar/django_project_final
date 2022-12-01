from django import forms

from shop.models import Shop

class ShopForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del producto",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "producto-name",
                "placeholder": "Nombre del producto",
                "required": "True",
            }
        ),
    )
    modelo = forms.CharField(
        label="Modelo",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "shop-modelo",
                "placeholder": "Modelo",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "shop-email",
                "placeholder": "Correo de contacto",
                "required": "True",
            }
        ),
    )
    collection = forms.CharField(
        label="Colección:",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "shop-collection",
                "placeholder": "Colección",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Shop
        fields = ["name", "modelo", "email", "collection"]
