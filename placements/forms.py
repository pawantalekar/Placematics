from django import forms
from .models import PlacedStudent

class PlacementForm(forms.ModelForm):
    class Meta:
        model = PlacedStudent
        fields = ['company', 'placement_date', 'role', 'salary', 'status']
        widgets = {
            'placement_date': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(attrs={'step': '0.01'}),
        }