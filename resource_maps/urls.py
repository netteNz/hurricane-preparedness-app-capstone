from django.urls import path
from . import views

app_name = 'resource_maps'

urlpatterns = [
    path('map/', views.map_view, name='map_voting'),
    path('map-voting/', views.map_view, name='map_voting'),
    path('map-voting/<int:waypoint_id>/vote/<str:vote_option>/', views.vote_waypoint, name='vote_waypoint'),
    path('map-voting/<int:waypoint_id>/info/', views.waypoint_info, name='waypoint_info'),
]
