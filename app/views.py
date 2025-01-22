from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import exercise, calories, exercise_progress
from django.urls import reverse_lazy
from datetime import date
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'app/home.html'
    

class ExerciseListView(LoginRequiredMixin,ListView):
    model = exercise
    context_object_name = 'exercises'
    template_name = 'app/exercise.html'

    def get_queryset(self):
        return exercise.objects.filter(user=self.request.user)


class ExerciseDetailView(LoginRequiredMixin,DetailView):
    model = exercise
    context_object_name = 'exercise'
    template_name = 'app/exercise_detail.html'

    def get_queryset(self):
        return exercise.objects.filter(user=self.request.user)

class exerciseCreateView(LoginRequiredMixin,CreateView):
    model = exercise
    fields = ['exercise_name', 'exercise_type', 'calorie_burn']
    template_name = 'app/exercise_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return exercise.objects.filter(user=self.request.user)

class ExerciseUpdateView(LoginRequiredMixin,UpdateView):
    model = exercise
    fields = ['exercise_name', 'exercise_type', 'calorie_burn']
    template_name = 'app/exercise_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return exercise.objects.filter(user=self.request.user)

class ExerciseDeleteView(LoginRequiredMixin,DeleteView):
    model = exercise
    template_name = 'app/exercise_delete.html'
    success_url = reverse_lazy('exercise')

    def get_queryset(self):
        return exercise.objects.filter(user=self.request.user)

class CaloriesListView(LoginRequiredMixin,ListView):
    model = calories
    context_object_name = 'calories'
    template_name = 'app/calories.html'

    def get_queryset(self):
        selected_date = self.request.GET.get('date')
        current_user = self.request.user 

        if selected_date:
            return calories.objects.filter(date=selected_date, user=current_user)
        else:
            return calories.objects.filter(date=date.today(), user=current_user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        selected_date = self.request.GET.get('date')
        current_user = self.request.user 

        if selected_date:
            filtered_calories = calories.objects.filter(date=selected_date, user=current_user)
        else:
            filtered_calories = calories.objects.filter(date=date.today(), user=current_user)
        
        total_count = filtered_calories.aggregate(Sum('calorie_count'))
        total_calories = total_count['calorie_count__sum'] or 0 
        
        context['total_calories'] = total_calories
        context['selected_date'] = selected_date or date.today()
        
        return context

class CaloriesDetailView(LoginRequiredMixin,DetailView):
    model = calories 
    context_object_name = 'calories'
    template_name = 'app/calories_detail.html'

    def get_queryset(self):
        return calories.objects.filter(user=self.request.user)

class CaloriesCreateView(LoginRequiredMixin,CreateView):
    model = calories
    fields = ['date', 'food_name', 'calorie_count']
    template_name = 'app/calories_create.html'
    success_url = reverse_lazy('calories')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
    
    def get_queryset(self):
        return calories.objects.filter(user=self.request.user)
    
class CaloriesUpdateView(LoginRequiredMixin,UpdateView):
    model = calories
    fields = ['date', 'food_name', 'calorie_count']
    template_name = 'app/calories_update.html'
    success_url = reverse_lazy('calories')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return calories.objects.filter(user=self.request.user)


class CaloriesDeleteView(LoginRequiredMixin,DeleteView):
    model = calories
    template_name = 'app/calories_delete.html'
    success_url = reverse_lazy('calories')

    def get_queryset(self):
        return calories.objects.filter(user=self.request.user)

class WorkoutLogListView(LoginRequiredMixin,ListView):
    model = exercise_progress
    context_object_name = 'workout_log'
    template_name = 'app/workout_log.html'

class WorkoutLogCreateView(LoginRequiredMixin, CreateView):
    model = exercise_progress
    fields = ['exercise_id', 'exercise_duration', 'weight_lifted']
    template_name = 'app/workout_log_create.html'
    success_url = reverse_lazy('workout')

    def get_queryset(self):
        return exercise_progress.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class WorkoutLogDetailView(LoginRequiredMixin, DetailView):
    model = exercise_progress 
    context_object_name = 'exercise_progress'
    template_name = 'app/workout_log_detail.html'

    def get_queryset(self):
        return exercise_progress.objects.filter(user=self.request.user)

class WorkoutLogUpdateView(LoginRequiredMixin, UpdateView):
    model = exercise_progress
    fields = ['exercise_id', 'exercise_duration', 'calories_burned', 'weight_lifted'] 
    template_name = 'app/workout_log_update.html'
    success_url = reverse_lazy('workout')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return exercise_progress.objects.filter(user=self.request.user)
    
class WorkoutLogDeleteView(LoginRequiredMixin, DeleteView):
    model = exercise_progress
    template_name = 'app/workout_log_delete.html'
    success_url = reverse_lazy('workout')

    def get_queryset(self):
        return exercise_progress.objects.filter(user=self.request.user)
