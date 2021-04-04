from django.forms import ModelForm
from .models import Order, Furniture, Customer


class FurnitureForm(ModelForm):
    class Meta:
        model = Furniture
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'