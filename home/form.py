from django import forms
from home.models import Product, CustomUser
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ('rating',)

class CustomUserForm(UserCreationForm):
    class Meta :
        model = CustomUser
        fields = ('email', 'name', 'date_of_birth', 'phone_number', 'address')

