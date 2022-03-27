from django import forms
from .models import Inquiry

class Inquiry_form(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'user_inquiry',
            
            'user_listing'
        ]
        
        
        