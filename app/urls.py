from django.urls import path
from .views import (HomePageView,ExerciseListView,ExerciseDetailView,
                    exerciseCreateView,ExerciseUpdateView, ExerciseDeleteView, 
                    CaloriesListView, CaloriesDetailView, CaloriesCreateView,CaloriesDeleteView,
                    CaloriesUpdateView)

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home' ),
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


]