from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('joy', '😊 Joyful'),
        ('peaceful', '😌 Peaceful'),
        ('excited', '🤗 Excited'),
        ('content', '😊 Content'),
        ('neutral', '😐 Neutral'),
        ('anxious', '😰 Anxious'),
        ('sad', '😢 Sad'),
        ('frustrated', '😤 Frustrated'),
        ('tired', '😴 Tired'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    intensity = models.IntegerField(default=5, help_text="1-10 scale")
    note = models.TextField(
        blank=True,
        help_text="Optional notes about your mood"
    )
    other_mood = models.CharField(
        max_length=100,
        blank=True,
        help_text="If mood is 'other', describe it"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Mood Entry"
        verbose_name_plural = "Mood Entries"

    def __str__(self):
        mood_display = self.get_mood_display()
        date_str = self.created_at.strftime('%Y-%m-%d')
        return f"{self.user.username} - {mood_display} ({date_str})"
