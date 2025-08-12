from django.contrib import admin
from .models import MoodEntry

# Register your models here.


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood', 'intensity', 'created_at')
    list_filter = ('user', 'mood', 'created_at')
    search_fields = ('user__username', 'mood__name',)
