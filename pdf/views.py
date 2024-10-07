from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import DocumentoPDFForm

def cargar_pdf(request):
    if request.method == 'POST':
        form = DocumentoPDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Esto debería subir el archivo a R2
            return redirect('success')
    else:
        form = DocumentoPDFForm()
    return render(request, 'cargar_pdf.html', {'form': form})

def success(request):
    return render(request, 'success.html')

