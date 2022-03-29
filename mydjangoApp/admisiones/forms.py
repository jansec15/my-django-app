from django import forms



class ImportarPaciente(forms.Form):
    archivo = forms.FileField()
    
