from django.db import models

class WeatherSummary(models.Model):
    date = models.DateField()
    temp_day = models.DecimalField(max_digits=5, decimal_places=2)
    temp_night = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f"Weather on {self.date}: {self.description}"

class WeatherDetail(models.Model):
    summary = models.ForeignKey(WeatherSummary, related_name='details', on_delete=models.CASCADE)
    temperature = models.JSONField()  # Assuming temperature might have multiple fields like min, max etc.
    feels_like = models.JSONField()  # JSONField is useful for nested data like day/night feels like temps
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    weather = models.CharField(max_length=255)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    wind_deg = models.IntegerField()
    cloudiness = models.IntegerField()
    rain = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Detailed Weather on {self.summary.date}"
