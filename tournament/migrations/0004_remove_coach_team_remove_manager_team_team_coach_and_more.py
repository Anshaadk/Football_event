# Generated by Django 4.2.5 on 2023-10-04 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_coach_manager_teammember_remove_gamescards_game_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='team',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tournament.coach'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='manager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tournament.manager'),
            preserve_default=False,
        ),
    ]