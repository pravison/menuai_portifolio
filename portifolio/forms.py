from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'subject', 'message' ]
        labels ={
           'name' :'Name', 
           'phone' :'Phone ', 
           'subject' :'Subject', 
           'message':'Message' 
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}), 
            'phone' : forms.NumberInput(attrs={'class':'form-control'}), 
            'subject' : forms.TextInput(attrs={'class':'form-control'}), 
            'message' : forms.TextInput(attrs={'class':'form-control'}),
        }