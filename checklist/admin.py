from django.contrib import admin
from .models import StaticChecklistItem, StaticChecklistCompletion


@admin.register(StaticChecklistItem)
class StaticChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('key', 'description', 'priority')


@admin.register(StaticChecklistCompletion)
class StaticChecklistCompletionAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'completed')
