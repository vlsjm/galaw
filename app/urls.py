from django.urls import path
from .views import (HomePageView,ExerciseListView,ExerciseDetailView,
                    exerciseCreateView,ExerciseUpdateView, ExerciseDeleteView, 
                    CaloriesListView, CaloriesDetailView, CaloriesCreateView,CaloriesDeleteView,
                    CaloriesUpdateView, WorkoutLogListView, WorkoutLogCreateView, WorkoutLogDetailView,
                    WorkoutLogUpdateView, WorkoutLogDeleteView,
                    HealthProfileDetailView, HealthProfileUpdateView, HealthProfileCreateView,WeightLossDashboardView,
                    WeightGoalCreateView, WeightGoalDeleteView, WeightGoalListView, WeightGoalUpdateView
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/',HomePageView.as_view(), name = 'home' ),
    path('exercise/',ExerciseListView.as_view(), name = 'exercise'),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name ='exercise_detail'),
    path('exercise/create', exerciseCreateView.as_view(), name = 'exercise_create'),
    path('exercise/<int:pk>/update', ExerciseUpdateView.as_view(), name ='exercise_update'),
    path('exercise/<int:pk>/delete', ExerciseDeleteView.as_view(), name ='exercise_delete'),
    path('calories/', CaloriesListView.as_view(), name = 'calories'),
    path('calories/<int:pk>/', CaloriesDetailView.as_view(), name = 'calories_detail'),
    path('calories/create', CaloriesCreateView.as_view(), name = 'calories_create'),
    path('calories/<int:pk>/update', CaloriesUpdateView.as_view(), name ='calories_update'),
    path('calories/<int:pk>/delete', CaloriesDeleteView.as_view(), name ='calories_delete'),
    path('workout/', WorkoutLogListView.as_view(), name = 'workout'),
    path('workout/<int:pk>/', WorkoutLogDetailView.as_view(), name ='workout_log_detail'),
    path('workout/create', WorkoutLogCreateView.as_view(), name = 'workout_log_create'),
    path('workout/<int:pk>/update', WorkoutLogUpdateView.as_view(), name ='workout_log_update'),
    path('workout/<int:pk>/delete', WorkoutLogDeleteView.as_view(), name ='workout_log_delete'),
    path('health_profile/', HealthProfileDetailView.as_view(), name = 'health_profile'),
    path('health_profile/create', HealthProfileCreateView.as_view(), name = 'health_profile_create'),
    path('health_profile/<int:pk>/update', HealthProfileUpdateView.as_view(), name ='health_profile_update'),
    path('weight_loss/', WeightLossDashboardView.as_view(), name='weight_loss_dashboard'),
    path('weight_goal/', WeightGoalListView.as_view(), name='weight_goal_list'),
    path('weight_goal/create/', WeightGoalCreateView.as_view(), name='weight_goal_create'),
    path('weight_goal/<int:pk>/update/', WeightGoalUpdateView.as_view(), name='weight_goal_update'),
    path('weight_goal/<int:pk>/delete/', WeightGoalDeleteView.as_view(), name='weight_goal_delete'),
]