from django.urls import path
from . import views

app_name = 'moods'

urlpatterns = [
    path('', views.mood_list, name='list'),
    path('add/', views.mood_add, name='add'),
    path('<int:pk>/', views.mood_detail, name='detail'),
    path('<int:pk>/edit/', views.mood_edit, name='edit'),
    path('<int:pk>/delete/', views.mood_delete, name='delete'),
]
