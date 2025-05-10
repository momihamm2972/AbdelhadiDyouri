from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('okay', 'Okay'),
        ('angry', 'Angry'),
        ('excited', 'Excited'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)  # Store mood like 'smile' or 'angry'
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} - {self.date}"
