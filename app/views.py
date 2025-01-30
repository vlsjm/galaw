from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import exercise, calories, exercise_progress, weightGoal, HealthProfile
from django.urls import reverse_lazy
from datetime import date
from django.db.models import Sum, Count, Avg
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        calorie_stats = calories.objects.filter(user=user).aggregate(
            total_calories_consumed=Sum('calorie_count')
        )

        calories_burned = exercise_progress.objects.filter(user=user).aggregate(
            total_calories_burned=Sum('calories_burned')
        )

        sessions_completed = exercise_progress.objects.filter(user=user).aggregate(
            total_sessions_completed=Count('exercise_id')
        )

        # average_calorie = calories.objects.filter(user=user).values('date').annotate(
        #      average_calories=Avg('calorie_count'))

        context['total_calories_consumed'] = calorie_stats['total_calories_consumed'] or 0
        context['total_calories_burned'] = calories_burned['total_calories_burned'] or 0
        context['total_sessions_completed']=sessions_completed['total_sessions_completed'] or 0
        # context['average_calories']=average_calorie['average_calories'] or 0
        return context
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = exercise.EXERCISE_TYPES
        return context

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

    def get_queryset(self):
        return exercise_progress.objects.filter(user=self.request.user)

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = exercise.objects.filter(user=self.request.user) 
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        exercise = form.cleaned_data['exercise_id']
        exercise_duration = form.cleaned_data['exercise_duration']
        total_minutes = exercise_duration.total_seconds() / 60
        calories_burned = exercise.calorie_burn * total_minutes
        form.instance.calories_burned = calories_burned
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = exercise.objects.all() 
        return context
    
class WorkoutLogDeleteView(LoginRequiredMixin, DeleteView):
    model = exercise_progress
    template_name = 'app/workout_log_delete.html'
    success_url = reverse_lazy('workout')

    def get_queryset(self):
        return exercise_progress.objects.filter(user=self.request.user)
    
class HealthProfileDetailView(LoginRequiredMixin, DetailView):
    model = HealthProfile
    context_object_name = 'profile'
    template_name = 'app/health_profile.html'

    def get_object(self):
        return HealthProfile.objects.get(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        if profile.height > 0:
            bmi = round(profile.weight / (profile.height ** 2), 2)
        if bmi < 18.5:
            bmi_category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            bmi_category = 'Normal'
        elif 25 <= bmi < 29.9:
            bmi_category = 'Overweight'
        else:
            bmi_category = 'Obese'       
        context['rounded_height'] = round(profile.height), 2
        context['calculated_bmi'] = bmi
        context['calculated_bmi_category'] = bmi_category
        return context

class HealthProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = HealthProfile
    fields = ['height', 'weight'] 
    template_name = 'app/health_profile_update.html'
    success_url = reverse_lazy('health_profile')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return HealthProfile.objects.filter(user=self.request.user)

class HealthProfileCreateView(LoginRequiredMixin, CreateView):
    model = HealthProfile
    fields = ['height', 'weight']
    template_name = 'app/health_profile_create.html'
    success_url = reverse_lazy('health_profile')

    def get_queryset(self):
        return HealthProfile.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class WeightLossDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'app/weight_goal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        health_profile = HealthProfile.objects.filter(user=user).first()
        context['current_weight'] = health_profile.weight if health_profile else "Not Set"
        weight_goal = weightGoal.objects.filter(user=user).order_by('-start_date').first()
        if weight_goal:
            context['target_weight'] = weight_goal.target_weight
            context['daily_calorie_limit'] = self.calculate_daily_calorie_limit(health_profile.weight, weight_goal.target_weight)
        else:
            context['target_weight'] = None
            context['daily_calorie_limit'] = None
        today = date.today()
        current_calories = calories.objects.filter(user=user, date=today).aggregate(total_calories=Sum('calorie_count'))['total_calories']
        context['current_calories'] = current_calories if current_calories else 0

        if weight_goal:
            context['progress'] = self.get_progress_message(health_profile.weight, weight_goal.target_weight)
        else:
            context['progress'] = "No goal set."

        return context

    def calculate_daily_calorie_limit(self, current_weight, target_weight):
       

        daily_calorie_deficit = 500
        base_calories = 2000  
        return max(1200, base_calories - daily_calorie_deficit)  

    def get_progress_message(self, current_weight, target_weight):
        if current_weight > target_weight:
            return "You're on track! Keep maintaining your calorie deficit."
        elif current_weight == target_weight:
            return "Congratulations! You've reached your goal."
        else:
            return "Your weight is below target. Consider maintaining balance."
    
        
class WeightGoalListView(LoginRequiredMixin, ListView):
    model = weightGoal
    template_name = 'app/weight_goal_list.html'
    context_object_name = 'weight_goals'

    def get_queryset(self):
        return weightGoal.objects.filter(user=self.request.user)


class WeightGoalCreateView(LoginRequiredMixin, CreateView):
    model = weightGoal
    fields = ['goal_type', 'start_date', 'target_weight', 'target_date']
    template_name = 'app/weight_goal_form.html'
    success_url = reverse_lazy('weight_goal_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class WeightGoalUpdateView(LoginRequiredMixin, UpdateView):
    model = weightGoal
    fields = ['goal_type', 'start_date', 'target_weight', 'target_date']
    template_name = 'app/weight_goal_form.html'
    success_url = reverse_lazy('weight_goal_list')

class WeightGoalDeleteView(LoginRequiredMixin, DeleteView):
    model = weightGoal
    template_name = 'app/weight_goal_confirm_delete.html'
    success_url = reverse_lazy('weight_goal_list')
