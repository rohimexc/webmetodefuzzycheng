from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import *
from tkinter import Widget



class DForm(ModelForm):
    class Meta:
        model = Dmaksmin
        fields = '__all__'
        widgets = {
            
            'd1':forms.NumberInput(attrs={'class':'form-control', 'required': True}),
            'd2':forms.NumberInput(attrs={'class':'form-control', 'required': True}),
            }

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


