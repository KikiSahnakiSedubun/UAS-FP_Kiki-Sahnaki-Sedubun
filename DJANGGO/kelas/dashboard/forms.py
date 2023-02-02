from django.forms import ModelForm
from dashboard.models import Barang, Buku, Daftarbuku
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'
    
        widget = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            'stok':forms.NumberInput({'class':'form-control'}),
            'harga':forms.NumberInput({'class':'form-control'}),
            'link_gbr':forms.TextInput({'class':'form-control'}),
            'jenis_id':forms.Select({'class':'form-control'}),
        }
        

class FormBuku(ModelForm):
    class Meta :
        model=Buku
        fields='__all__'
    
        widget = {
            'nama':forms.TextInput({'class':'form-control'}),
            'stok':forms.NumberInput({'class':'form-control'}),
            'harga':forms.NumberInput({'class':'form-control'}),
            'jenis_id':forms.Select({'class':'form-control'}),
        }

class FormDaftarbuku(ModelForm):
    class Meta :
        model=Daftarbuku
        fields='__all__'
    
        widget = {
            'nama':forms.TextInput({'class':'form-control'}),
            'harga':forms.NumberInput({'class':'form-control'}),
        }