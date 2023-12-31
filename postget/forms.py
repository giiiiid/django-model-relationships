from django import forms
from .models import *

class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {"customer_name":forms.HiddenInput()}
