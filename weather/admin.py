from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
from .models import WeatherSummary, WeatherDetail

class WeatherDetailExportAdmin(ExportActionModelAdmin):
    pass

class WeatherDetailInline(admin.TabularInline):
    model = WeatherDetail
    extra = 1
    fields = ['temperature', 'feels_like', 'pressure', 'humidity', 'weather', 'wind_speed', 'wind_deg', 'cloudiness', 'rain']
    show_change_link = True

# This is the class that needs to inherit from ImportExportModelAdmin
class WeatherSummaryAdmin(ImportExportModelAdmin):
    list_display = ('date', 'temp_day', 'temp_night', 'description')
    list_filter = ('date',)
    search_fields = ('description',)
    inlines = [WeatherDetailInline]

# If you want to provide import/export functionality for WeatherDetail as well:
@admin.register(WeatherDetail)
class WeatherDetailAdmin(ImportExportModelAdmin):
    list_display = ['summary', 'temperature', 'feels_like', 'pressure', 'humidity', 'weather', 'wind_speed', 'wind_deg', 'cloudiness', 'rain']
    search_fields = ['summary__date', 'weather']
    list_filter = ['summary__date', 'weather']