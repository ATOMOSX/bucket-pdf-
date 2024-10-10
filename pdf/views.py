
# Create your views here.

import boto3
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .forms import FileUploadForm


# Configura el cliente de boto3 con las credenciales de Cloudflare R2
def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=settings.CLOUDFLARE_R2_ACCESS_KEY_ID,
        aws_secret_access_key=settings.CLOUDFLARE_R2_SECRET_ACCESS_KEY,
        endpoint_url=settings.CLOUDFLARE_R2_ENDPOINT_URL
    )


def upload_file_to_r2(file, filename):
    s3_client = get_s3_client()
    bucket_name = settings.CLOUDFLARE_R2_BUCKET_NAME

    # Sube el archivo a R2 (similar a S3)
    s3_client.upload_fileobj(file, bucket_name, filename)

    # Devuelve la URL del archivo subido
    file_url = f"{settings.CLOUDFLARE_R2_ENDPOINT_URL}/{bucket_name}/{filename}"
    return file_url


# Vista para subir el archivo
def upload_file_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file = request.FILES.get('file', None)

                if file is None:
                    return JsonResponse({'success': False, 'error': 'No file was provided.'})

                # Verificamos que file.name no sea None
                filename = file.name
                if filename is None or filename == '':
                    return JsonResponse({'success': False, 'error': 'The file does not have a valid name.'})

                # Subimos el archivo a R2
                file_url = upload_file_to_r2(file, filename)

                return JsonResponse({'success': True, 'file_url': file_url})
            except Exception as e:
                # Capturamos cualquier excepción y la retornamos como respuesta
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    form = FileUploadForm()
    return render(request, 'cargar_pdf.html', {'form':form})