from django import forms 
from .models import Ikasle,Ikasgaiak,Nota
class IkasleForm(forms.ModelForm):    
    class Meta:        
        model=Ikasle        
        fields=['izena','abizena','jaiotze_data']
class IkasgaiakForm(forms.ModelForm):    
    class Meta:        
        model=Ikasgaiak        
        fields=['izena','maila','hizkuntza']
class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota','oharra','ikasle_kodea', 'ikasgai_kodea']  # Campos que se mostrarán en el formulario

    # Opción para personalizar la apariencia del campo "ikasle"
    ikasle_kodea = forms.ModelChoiceField(queryset=Ikasle.objects.all(), label="Seleccionar Ikasle")
    ikasgai_kodea = forms.ModelChoiceField(queryset=Ikasgaiak.objects.all(), label="Seleccionar Ikasgai")
class NotaAldatuForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota', 'oharra']  # Solo permitimos editar 'nota' y 'oharra'