from django import forms
from django.contrib.auth.models import User
from .models import Chapa

class ChapaForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
                'username',
                'password',
                'email',
                'first_name',
                'last_name',
                
        )
        
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome de Usuario'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primeiro Nome'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ultimo Nome'}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}),
        }
        
        
class CreateChapaForm(forms.ModelForm):
    class Meta:
        model = Chapa
        fields = (
            'usuario',
            'estado',
            'cidade',
            'img',
            'descricao',
            'cel',

        )
        
        widgets = {
            'usuario':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario'}),
            'estado':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}),
            'cidade':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}),
            'img':forms.URLInput(attrs={'class':'form-control', 'placeholder':'Url'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'cel':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numero de WhatsApp'}),

        }
        