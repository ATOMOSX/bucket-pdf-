from django.urls import path
from .views import upload_file_view

urlpatterns = [
    path('upload/', upload_file_view, name='upload_file'),
]