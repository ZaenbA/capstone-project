from django.urls import path
from .views import (
    MoodEntryList, MoodEntryDetail, MoodEntryCreate, 
    MoodEntryUpdate, MoodEntryDelete
)

app_name = 'moods'  # important for namespacing

urlpatterns = [
    path('', MoodEntryList.as_view(), name='list'),
    path('add/', MoodEntryCreate.as_view(), name='add'),  # keeping 'add'
    path('<int:pk>/', MoodEntryDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', MoodEntryUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', MoodEntryDelete.as_view(), name='delete'),
]
