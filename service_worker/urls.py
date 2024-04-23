# service_worker/urls.py

from django.urls import path
from .views import service_worker

urlpatterns = [
    path('serviceworker.js', service_worker, name='service_worker'),
]
