from django import forms
from django.contrib.auth.models import User
from .models import Farmer

class FarmerSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Farmer
        fields = ['name', 'phone_number', 'location', 'acres']
    
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        farmer = super().save(commit=False)
        farmer.user = user
        if commit:
            farmer.save()
        return user

#farmers profile update form
class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'phone_number', 'location', 'acres']