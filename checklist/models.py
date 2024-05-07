from django.db import models


class StaticChecklistItem(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    key = models.CharField(max_length=50, unique=True)  # Unique identifier for static items
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.description


class StaticChecklistCompletion(models.Model):
    item = models.ForeignKey(StaticChecklistItem, on_delete=models.CASCADE)
    user = models.CharField(max_length=50, default='anonymous')  # Replace with a user model if needed
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item.key} - {self.user}'
