from django import forms
from .models import Contact , Sent

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
        model = Sent
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
        }