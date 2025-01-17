# Generated by Django 5.1.3 on 2025-01-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_exercise_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calories',
            old_name='calorie_intake',
            new_name='calories',
        ),
        migrations.AddField(
            model_name='calories',
            name='food_name',
            field=models.CharField(default=12, max_length=20),
            preserve_default=False,
        ),
    ]
