from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page_view(request):
    return render(request, 'home.html')


@login_required
def dashboard_view(request):
    """Dashboard view for authenticated users"""
    from moods.models import MoodEntry
    
    # Get the 3 most recent mood entries for this user
    recent_entries = MoodEntry.objects.filter(
        user=request.user
    ).order_by('-created_at')[:3]
    
    context = {
        'recent_entries': recent_entries,
    }
    return render(request, 'dashboard.html', context)


class CustomLoginView(auth_views.LoginView):
    """Custom login view with success message"""
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        username = user.first_name or user.username
        messages.success(
            self.request,
            f'Welcome back, {username}! You have successfully logged in.'
        )
        return super().form_valid(form)


class CustomLogoutView(auth_views.LogoutView):
    """Custom logout view with success message"""
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = request.user.first_name or request.user.username
            messages.success(
                request,
                f'Goodbye, {username}! You have been successfully logged out.'
            )
        return super().dispatch(request, *args, **kwargs)