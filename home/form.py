from django import forms
from home.models import Product

class ProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ('rating',)