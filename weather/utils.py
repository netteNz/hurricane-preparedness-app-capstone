from django.core.exceptions import ValidationError
from django.conf import settings as SETTINGS
from datetime import datetime
import logging
import requests


logger = logging.getLogger(__name__)

def fetch_weather_data(city, api_key, detail_level=False):
    api_key = SETTINGS.API_KEY
    url = f"https://pro.openweathermap.org/data/2.5/forecast/climate?q={city}&appid={api_key}&units=metric&cnt=14"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        data = response.json()

        summary_data = []
        detailed_data = []

        for day in data['list']:
            # Common data parsing
            date = datetime.fromtimestamp(day['dt']).date()
            temp_day = day['temp']['day']
            temp_night = day['temp']['night']
            description = day['weather'][0]['description']
            icon = day['weather'][0]['icon'] + ".svg"  # Append ".png" to the icon code

            summary = {
                'date': date,
                'temp_day': temp_day,
                'temp_night': temp_night,
                'description': description,
                'icon': icon
            }
            summary_data.append(summary)

            if detail_level:
                # Detailed data parsing includes all relevant fields
                detailed_info = {
                    'date': date,
                    'temperature': day['temp'],
                    'feels_like': day['feels_like'],
                    'pressure': day['pressure'],
                    'humidity': day['humidity'],
                    'weather': day['weather'],
                    'wind_speed': day['speed'],
                    'wind_deg': day['deg'],
                    'cloudiness': day['clouds'],
                    'rain': day.get('rain', 0)  # Handle possible absence of rain data
                }
                # Update icon in detailed info
                detailed_info['weather'][0]['icon'] = detailed_info['weather'][0]['icon'] + ".png"
                detailed_data.append(detailed_info)

        return summary_data, detailed_data
    
    except requests.HTTPError as e:
        logger.error(f"HTTP Error: {e.response.status_code} for city {city}")
        raise ValidationError("There was a problem fetching the weather data.")
    except requests.RequestException as e:
        logger.error(f"Request Error: {str(e)}")
        raise ValidationError("A network error occurred.")
    except Exception as e:
        logger.error(f"General Error: {str(e)}")
        raise ValidationError("An unexpected error occurred.")
    


# The function calls are commented out to adhere to the guidelines.
