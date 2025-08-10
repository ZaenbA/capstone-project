from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignupForm

# Create your views here.

class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account created successfully. Please log in.")
        return super().form_valid(form)