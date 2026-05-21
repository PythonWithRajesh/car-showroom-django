from django import forms
from .models import Delivery
from datetime import date

class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['delivery_date'].initial = date.today()

        self.fields['delivery_date'].widget = forms.DateInput(
            attrs={
                'type': 'date'   # ✅ calendar popup આવશે
            }
        )