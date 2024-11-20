from django import forms 
from .models import Kotxe,Pertsona,Alokairua
class KotxeForm(forms.ModelForm):    
    class Meta:        
        model=Kotxe        
        fields=['marka','modeloa','kilometroak']
class AlokairuForm(forms.ModelForm):    
    class Meta:
        model = Alokairua
        fields = ['alokairu_data_hasi','alokairu_data_bukatu'] 
    pertsona = forms.ModelChoiceField(queryset=Pertsona.objects.all(), label="Seleccionar Pertsona")
    kotxea = forms.ModelChoiceField(queryset=Kotxe.objects.all(), label="Seleccionar Kotxe")
class PertsonaForm(forms.ModelForm):    
    class Meta:        
        model=Pertsona        
        fields=['izena','abizena','emaila']