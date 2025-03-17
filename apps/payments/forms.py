from django import forms
from .models import Payment


# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['payment_method']
#

class CreditCardForm(forms.Form):
    card_number = forms.CharField(max_length=16, min_length=16, widget=forms.TextInput(attrs={
        'placeholder': 'Card Number',
        'class': 'border p-2 w-full rounded-lg'
    }))
    expiry_date = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'MM/YY',
        'class': 'border p-2 w-full rounded-lg'
    }))
    cvv = forms.CharField(max_length=3, widget=forms.PasswordInput(attrs={
        'placeholder': 'CVV',
        'class': 'border p-2 w-full rounded-lg'
    }))