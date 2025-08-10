from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignupForm

# Create your views here.

def mood_list(request):
    """View to list all moods"""
    return render(request, 'moods/mood_list.html')


def mood_add(request):
    """View to add a new mood"""
    return render(request, 'moods/mood_add.html')


def mood_detail(request, pk):
    """View to show mood details"""
    return render(request, 'moods/mood_detail.html')


def mood_edit(request, pk):
    """View to edit a mood"""
    return render(request, 'moods/mood_edit.html')


def mood_delete(request, pk):
    """View to delete a mood"""
    return render(request, 'moods/mood_delete.html')


class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 
            "Account created successfully. Please log in."
        )
        return super().form_valid(form)