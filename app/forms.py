from django import forms
from .models import Customer,Room,Service
from django import forms


class ProfileForm(forms.Form):
    name=forms.CharField(label="enter name",max_length=100)
    email=forms.CharField(label="enter email",max_length=100)
    phone=forms.CharField(label="phone",max_length=100)
    address=forms.CharField(label="address",max_length=100)
    room_display = forms.ModelMultipleChoiceField(queryset=Room.objects.all())
    adhaar=forms.ImageField()
    
class ServiceForm(forms.Form):
    cust_display = forms.ModelMultipleChoiceField(queryset=Customer.objects.all())
    service_display = forms.ModelMultipleChoiceField(queryset=Service.objects.all())
