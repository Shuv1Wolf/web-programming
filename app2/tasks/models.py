from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Модель задачи для пользователя."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
