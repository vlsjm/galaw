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
    calories_burned = models.FloatField(null=True, blank=True)
    weight_lifted = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.exercise_id.exercise_name
    
    
class calories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food_name = models.CharField(max_length=20)
    calorie_count = models.FloatField()

    def __str__(self):
        return self.food_name

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
    
class HealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(null=False, blank=False, help_text="Height in meters (e.g., 1.80)")
    weight = models.FloatField(null=False, blank=False, help_text="Weight in kilograms (e.g., 65)")
    bmi = models.FloatField(editable=False, null=True)
    bmi_classification_type= [
        ('uw','Under Weight'),
        ('hw','Healthy Weight'),
        ('ow', 'Over Weight'),
        ('ob', 'Obesity'),
    ]
    bmi_type = models.CharField(max_length=20, choices=bmi_classification_type, editable=False, null=True)
