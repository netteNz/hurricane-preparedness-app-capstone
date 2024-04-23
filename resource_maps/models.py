from django.db import models
from django.db.models import Q, Count
from django.contrib.auth.models import User
from django.utils import timezone


class ResourceCategory(models.Model):
    type = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type

class Waypoint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.ForeignKey(ResourceCategory, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    votes_yes = models.IntegerField(default=0)
    votes_no = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def tally_votes(self):
        # Returns a dictionary with the total present and absent votes
        votes = self.votes.aggregate(
            present_count=Count('id', filter=Q(vote=True)),
            absent_count=Count('id', filter=Q(vote=False))
        )
        return votes

    def vote_score(self):
        # A simple vote score might just be present votes minus absent votes
        return self.votes_yes - self.votes_no


    def vote_percentage(self):
        # Calculates the percentage of yes votes
        total_votes = self.votes_yes + self.votes_no
        if total_votes == 0:
            return 0  # Avoid division by zero
        return (self.votes_yes / total_votes) * 100

    def __str__(self):
        return f"{self.name} at {self.latitude}, {self.longitude}"


class Vote(models.Model):
    waypoint = models.ForeignKey(Waypoint, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(auto_now_add=True)
    vote = models.BooleanField()  # True for resource present, False for resource absent

    class Meta:
        unique_together = ('waypoint', 'user', 'vote_date')  # Ensures unique votes per user per day

    def __str__(self):
        return f"Vote by {self.user} for {self.waypoint.name} as {'present' if self.vote else 'absent'}"
