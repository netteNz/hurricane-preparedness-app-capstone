from django.urls import path
from . import views

urlpatterns = [
    path('', views.static_checklist, name='static_checklist'),
    path('toggle/<int:item_id>/', views.toggle_static_item, name='toggle_static_item'),
]
