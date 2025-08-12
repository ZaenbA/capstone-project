from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MoodEntry


class SignupForm(UserCreationForm):
    """
    Extended user registration form that includes email field.
    Inherits from Django's built-in UserCreationForm and adds email
    requirement.
    """
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        """
        Save the user instance with the provided email address.
        
        Args:
            commit (bool): Whether to save the user to the database immediately
            
        Returns:
            User: The created user instance
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class MoodEntryForm(forms.ModelForm):
    """
    Form for creating and editing mood entries.
    Allows users to record their mood, intensity level, and optional notes.
    """
    class Meta:
        model = MoodEntry
        fields = ['mood', 'intensity', 'note', 'other_mood']
