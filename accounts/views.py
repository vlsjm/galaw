from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class RegisterCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html' 
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Automatically log in the user after registration
        return redirect(self.success_url)
