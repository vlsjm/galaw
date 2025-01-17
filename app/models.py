from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=50, null=True, blank=True)
    EXERCISE_TYPES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility','Flexibility'),
        ('balance', 'Balance'),
        ('hiit', 'High-Intensity Interval Training'),
        ('other', 'Others')

    ]
    exercise_type = models.CharField(max_length=50, choices=EXERCISE_TYPES)
    calorie_burn = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.exercise_name
    
    def get_absolute_url(self):
       return reverse("exercise_detail", kwargs={"pk": self.pk})

class exercise_progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(exercise, on_delete=models.CASCADE)
    exercise_date = models.DateTimeField(auto_now_add=True)
    exercise_duration = models.DurationField(null=False, blank=False)
    calories_burned = models.FloatField(null=False, blank=False)

def save(self, *args, **kwargs):
   
        if self.exercise_id and self.exercise_duration:
            duration_in_minutes = self.exercise_duration.total_seconds() / 60
            self.calories_burned = duration_in_minutes * self.exercise_id.calorie_burn
        super().save(*args, **kwargs)

        def __str__(self):
         return f"{self.user.username} - {self.exercise_id.exercise_name} on {self.exercise_date}"
    
class calories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food_name = models.CharField(max_length=20)
    calorie_count = models.FloatField()

    def __str__(self):
        return self.food_name
    
#widget=forms.DateInput(attrs={'type': 'date'}), label="Date"

class weightGoal(models.Model):
    GOAL_TYPES = [
        ('maintain','Maintain Weight'),
        ('weight gain','Weight Gain'),
        ('weight loss', 'Weight Loss'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPES)
    start_date = models.DateField()
    target_weight = models.FloatField()
    target_date = models.DateField()

    def __str__(self):
        return f"{self.goal_type}"
    
class FitnessAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    daily_avg_calorie = models.FloatField()
    weekly_exercise_duration = models.DurationField()
    weight_change = models.FloatField()

class HealthProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    bmi_classification_type= [
        ('uw','Under Weight'),
        ('hw','Healthy Weight'),
        ('ow', 'Over Weight'),
        ('ob', 'Obesity'),
    ]
    bmi_type = models.CharField(max_length=20, choices=bmi_classification_type)


