from django import forms
from .models import Followup


class FollowupForm(forms.ModelForm):

    class Meta:

        model = Followup

        fields = '__all__'

        widgets = {

            'followup_date': forms.DateInput(attrs={
                'type': 'date'
            }),

        }