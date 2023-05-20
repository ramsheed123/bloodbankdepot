from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    last_donation_date = forms.DateField(
        label='Last Blood Donation Date',
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
        required=False
    )

    class Meta:
        model = Registration
        fields = '__all__'
