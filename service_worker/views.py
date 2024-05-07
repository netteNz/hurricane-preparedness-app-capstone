# service_worker/views.py

from django.http import HttpResponse
import os


def service_worker(request):
    # Assuming your serviceworker.js is in the static root
    with open(os.path.join('static', 'serviceworker.js'), 'rb') as f:
        response = HttpResponse(f, content_type="application/javascript")
        response['Service-Worker-Allowed'] = '/'
    
    return response
