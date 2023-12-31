# Generated by Django 4.2.6 on 2023-10-05 09:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0021_confomed_team_alter_match_team1_alter_match_team2'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='started_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='tournament_end',
            field=models.BooleanField(default=False),
        ),
    ]
