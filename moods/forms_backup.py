from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MoodEntry


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'intensity', 'note', 'other_mood']
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-select'}),
            'intensity': forms.NumberInput(attrs={
                'class': 'form-range', 
                'min': 1, 
                'max': 10, 
                'type': 'range'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3,
                'placeholder': 'What triggered this feeling? Any thoughts to remember...'
            }),
            'other_mood': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your mood...',
                'style': 'display:none;'
            })
        }