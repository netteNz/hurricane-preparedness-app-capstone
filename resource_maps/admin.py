from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ResourceCategory, Waypoint, Vote


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ['type', 'description']
    search_fields = ['type']

@admin.register(Waypoint)
class WaypointAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'latitude', 'longitude', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'category']
    search_fields = ['name', 'description', 'category__type']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['waypoint', 'user', 'vote', 'vote_date']
    list_filter = ['vote', 'vote_date', 'waypoint__name']
    search_fields = ['waypoint__name', 'user__username']

#@admin.register(WaypointImportExport)
class YourModelAdmin(ImportExportModelAdmin):
    pass
