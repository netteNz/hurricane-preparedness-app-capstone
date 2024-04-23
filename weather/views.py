from django.core.cache import cache
from django.core.serializers import serialize
from .models import WeatherDetail, WeatherSummary
from django.shortcuts import render, get_object_or_404
from django.conf import settings as SETTINGS
from .utils import fetch_weather_data  # Importing fetch_weather_data from utils.py
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def forecast(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')  # Default to empty string if no city is provided

        if not city:
            return render(request, 'weather/error.html', {'error_message': 'No city provided.'})
        
        api_key = SETTINGS.API_KEY  # Retrieve API key securely
        # Use the utility function to fetch data, focusing on detailed data
        summary_data, detailed_data = fetch_weather_data(city, api_key, detail_level=True)
        
        if detailed_data:  # Check if detailed data was successfully fetched
            context = {
                'city': city, 'detailed_data': detailed_data } # Pass detailed data to the template
            
            # Save the data to the database
            save_weather_data(summary_data, detailed_data)

            return render(request, 'weather/forecast_detailed.html', context)
        else:
            # If data fetch was not successful, use an error message
            return render(request, 'weather/error.html', {'error_message': 'Failed to retrieve detailed weather data.'})
    else:
        # Render a default or initial form view when not a POST request
        return render(request, 'weather/index.html')

def get_detailed_weather(request, date):
    # The request is required for Django's view function signature but is not used in the function logic.
    cache_key = f'weather_detailed_{date}'
    detailed_json = cache.get(cache_key)

    if not detailed_json:
        detailed = get_object_or_404(WeatherDetail, summary__date=date)
        detailed_json = serialize('json', [detailed])
        cache.set(cache_key, detailed_json, timeout=3600)  # cache for one hour
    return HttpResponse(detailed_json, content_type="application/json")

def get_weather_summary(request, date):
    # The request is required for Django's view function signature but is not used in the function logic.
    cache_key = f'weather_summary_{date}'
    summary_json = cache.get(cache_key)
    
    if not summary_json:
        summary = get_object_or_404(WeatherSummary, date=date)
        summary_json = serialize('json', [summary])
        cache.set(cache_key, summary_json, timeout=3600)  # Cache for one hour
    
    return HttpResponse(summary_json, content_type="application/json")

def save_weather_data(summary_data, detailed_data):
    for summary in summary_data:
        # Update or create summary entries
        weather_summary, created = WeatherSummary.objects.update_or_create(
            date=summary['date'],
            defaults={
                'temp_day': summary['temp_day'],
                'temp_night': summary['temp_night'],
                'description': summary['description'],
                'icon': summary['icon']
            }
        )

        # Only proceed with details if required
        if detailed_data:
            for detail in detailed_data:
                if detail['date'] == summary['date']:  # Ensure date matches
                    WeatherDetail.objects.update_or_create(
                        summary=weather_summary,
                        defaults={
                            'temperature': detail['temperature'],
                            'feels_like': detail['feels_like'],
                            'pressure': detail['pressure'],
                            'humidity': detail['humidity'],
                            'weather': detail['weather'][0]['main'],  # Simplify or adjust as needed
                            'wind_speed': detail['wind_speed'],
                            'wind_deg': detail['wind_deg'],
                            'cloudiness': detail['cloudiness'],
                            'rain': detail['rain']
                        }
                    )
