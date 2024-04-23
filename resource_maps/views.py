import json
from .models import Waypoint
from django.db.models import F
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
import logging

logger = logging.getLogger(__name__)



def map_view(request):
    waypoints = Waypoint.objects.filter(is_active=True)
    waypoints_json = serialize('json', waypoints)
    vote_scores = {waypoint.id: waypoint.vote_score() for waypoint in waypoints}
    vote_percentages = {waypoint.id: waypoint.vote_percentage() for waypoint in waypoints}

    context = {
        'waypoints_json': waypoints_json,
        'waypoints': waypoints,
        'vote_scores': vote_scores,
        'vote_percentages': vote_percentages,
    }

    return render(request, 'resource_maps/map_voting.html', context)


def waypoint_info(request, waypoint_id):
    waypoint = get_object_or_404(Waypoint, pk=waypoint_id)
    vote_score = waypoint.vote_score()
    vote_percentage = waypoint.vote_percentage()

    context = {
        'waypoint': waypoint,
        'vote_score': vote_score,
        'vote_percentage': vote_percentage,
    }

    return render(request, 'resource_maps/waypoint_info.html', context)

@require_http_methods(["POST"])
def vote_waypoint(request, waypoint_id, vote_type):
    logger.debug(f"Voting {vote_type} on waypoint {waypoint_id}")
    waypoint = get_object_or_404(Waypoint, pk=waypoint_id)
    # Updating votes to ensure thread safety
    if vote_type == 'yes':
        waypoint.votes_yes = F('votes_yes') + 1
    elif vote_type == 'no':
        waypoint.votes_no = F('votes_no') + 1
    waypoint.save()
    waypoint.refresh_from_db()  # Refresh the instance to get updated values from the database

    return JsonResponse({
        'waypoint_id': waypoint.id,
        'vote_score': waypoint.vote_score(),
        'vote_percentage': waypoint.vote_percentage()
    })

