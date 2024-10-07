from django import forms
from .models import DocumentoPDF

class DocumentoPDFForm(forms.ModelForm):
    class Meta:
        model = DocumentoPDF
        fields = ['archivo', 'nombre']  # Incluye los campos necesarios
