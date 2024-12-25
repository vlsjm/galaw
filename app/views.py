from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import exercise
from django.urls import reverse_lazy
 
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