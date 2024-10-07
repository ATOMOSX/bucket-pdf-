from django.db import models

class DocumentoPDF(models.Model):
    archivo = models.FileField(upload_to='pdfs/')  # Esto subirá el archivo a R2 usando el storage backend configurado
    nombre = models.CharField(max_length=255)
    subido_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
