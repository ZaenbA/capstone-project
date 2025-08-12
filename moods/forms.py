from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MoodEntry


class SignupForm(UserCreationForm):
    """This is a custom user registration form that also includes email field. 
    It inherits from Django's built in UserCreation Form as well as adding email requirements so that users can be updated if needed.
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
    This is a form for creating and editing mood entries for registered users.
    Allows users to record their mood, intensity level using a scale between 1 - 10, and optional notes to help them track more insights about their wellbeing.
    """
    class Meta:
        model = MoodEntry
        fields = ['mood', 'intensity', 'note', 'other_mood']
