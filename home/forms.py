from django import forms
from .models import contact,Bus,book

class contactform(forms.ModelForm):

    class Meta:
        model=contact
        fields=['name','email','message']
class bform(forms.ModelForm):

    class Meta:
        model=Bus
        exclude=['username','duration','seatno']   

class bookform(forms.ModelForm):

    class Meta:
        model=book
        exclude="__all__" 