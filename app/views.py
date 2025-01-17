from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import exercise, calories, exercise_progress
from django.urls import reverse_lazy
from datetime import date
from django.db.models import Sum

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class ExerciseListView(ListView):
    model = exercise
    context_object_name = 'exercises'
    template_name = 'app/exercise.html'

class ExerciseDetailView(DetailView):
    model = exercise
    context_object_name = 'exercise'
    template_name = 'app/exercise_detail.html'

class exerciseCreateView(CreateView):
    model = exercise
    fields = ['user','exercise_name', 'exercise_type', 'calorie_burn']
    template_name = 'app/exercise_create.html'

class ExerciseUpdateView(UpdateView):
    model = exercise
    fields = ['user','exercise_name', 'exercise_type', 'calorie_burn']
    template_name = 'app/exercise_update.html'

class ExerciseDeleteView(DeleteView):
    model = exercise
    template_name = 'app/exercise_delete.html'
    success_url = reverse_lazy('exercise')

class CaloriesListView(ListView):
    model = calories
    context_object_name = 'calories'
    template_name = 'app/calories.html'
    
    def get_queryset(self):
        selected_date = self.request.GET.get('date')

        if selected_date:
            return calories.objects.filter(date=selected_date)
        else:
            return calories.objects.filter(date=date.today())
        
        return render(request, 'app/calories.html', {
        'calories': calories,
        'specific_date': selected_date,
    })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        selected_date = self.request.GET.get('date')
        
        if selected_date:
            filtered_calories = calories.objects.filter(date=selected_date)
        else:
            filtered_calories = calories.objects.filter(date=date.today())
        
        total_count = filtered_calories.aggregate(Sum('calorie_count'))
        total_calories = total_count['calorie_count__sum']

        
        context['total_calories'] = total_calories
        context['selected_date'] = selected_date or date.today()
        
        return context

class CaloriesDetailView(DetailView):
    model = calories 
    context_object_name = 'calories'
    template_name = 'app/calories_detail.html'

class CaloriesCreateView(CreateView):
    model = calories
    fields = ['user','date', 'food_name', 'calorie_count']
    template_name = 'app/calories_create.html'
    success_url = reverse_lazy('calories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
    
class CaloriesUpdateView(UpdateView):
    model = calories
    fields = ['user','date', 'food_name', 'calorie_count']
    template_name = 'app/calories_update.html'
    success_url = reverse_lazy('calories')


class CaloriesDeleteView(DeleteView):
    model = calories
    template_name = 'app/calories_delete.html'
    success_url = reverse_lazy('calories')

class WorkoutLogListView(ListView):
    model = exercise_progress
    context_object_name = 'exercise_log'
    template_name = 'app/exercise_log.html'