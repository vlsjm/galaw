# Generated by Django 5.1.3 on 2025-01-05 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_calorie_intake_calories_calories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calories',
            old_name='calories',
            new_name='calorie_count',
        ),
    ]
