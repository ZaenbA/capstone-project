from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MoodEntry
from .forms import MoodEntryForm

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
        user = form.save()
        messages.success(
            self.request,
            f"Welcome to Mindful Moments+, {user.first_name or user.username}! "
            "Your account has been created successfully. Please log in."
        )
        return super().form_valid(form)

class MoodEntryList(LoginRequiredMixin, ListView):
    template_name = 'moods/mood_list.html'
    context_object_name = 'entries'
    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)

class MoodEntryDetail(LoginRequiredMixin, DetailView):
    template_name = 'moods/mood_detail.html'
    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)

class MoodEntryCreate(LoginRequiredMixin, CreateView):
    form_class = MoodEntryForm
    template_name = 'moods/mood_add.html'  # Use existing template
    success_url = reverse_lazy('moods:list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        r = super().form_valid(form)
        messages.success(self.request, "Mood saved.")
        return r

class MoodEntryUpdate(LoginRequiredMixin, UpdateView):
    form_class = MoodEntryForm
    template_name = 'moods/mood_form.html'
    success_url = reverse_lazy('moods:list')
    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)
    def form_valid(self, form):
        r = super().form_valid(form)
        messages.success(self.request, "Mood updated.")
        return r

class MoodEntryDelete(LoginRequiredMixin, DeleteView):
    template_name = 'moods/mood_confirm_delete.html'
    success_url = reverse_lazy('moods:list')
    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)
    def delete(self, request, *a, **kw):
        messages.success(self.request, "Mood deleted.")
        return super().delete(request, *a, **kw)