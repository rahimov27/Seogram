from django import forms
from django.forms import widgets
from .models import Contact, SendEmail , Sent



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
        }
class SentForm(forms.ModelForm):
    class Meta:
        model = SendEmail
        fields = '__all__'
        widgets = {
            'email' : forms.TextInput(attrs={'class':'form-control'})
        }