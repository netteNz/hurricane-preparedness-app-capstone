from django.db import models


# Create your models here.
class ChecklistItem(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
