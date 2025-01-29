from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class RegisterCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'  # Your registration template
    success_url = reverse_lazy('home')  # Redirect after successful registration

    def form_valid(self, form):
        # Save user and log them in
        user = form.save()
        login(self.request, user)  # Log the user in automatically
        return redirect(self.success_url)
