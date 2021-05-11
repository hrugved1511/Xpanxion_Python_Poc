from django import forms
from apipaths.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"