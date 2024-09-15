from django import forms
from .models import Order

class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product','number_of_items')