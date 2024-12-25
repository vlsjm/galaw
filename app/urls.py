from django.urls import path
from .views import (HomePageView,ExerciseListView,ExerciseDetailView,
                    exerciseCreateView,ExerciseUpdateView, ExerciseDeleteView)

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home' ),
    path('exercise/',ExerciseListView.as_view(), name = 'exercise'),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name ='exercise_detail'),
    path('exercise/create', exerciseCreateView.as_view(), name = 'exercise_create'),
    path('exercise/<int:pk>/update', ExerciseUpdateView.as_view(), name ='exercise_update'),
    path('exercise/<int:pk>/delete', ExerciseDeleteView.as_view(), name ='exercise_delete'),

]