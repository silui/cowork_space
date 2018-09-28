from django import forms
# from .forms import ProductForm
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title','description','price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
