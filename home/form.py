from django import forms
from home.models import Product, CustomUser

class ProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ('rating',)

class CustomUserForm(forms.ModelForm):
    class Meta :
        model = CustomUser
        fields = ('user', 'birthday', 'phone_number', 'address', 'sex')