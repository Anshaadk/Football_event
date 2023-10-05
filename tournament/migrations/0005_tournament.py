# Generated by Django 4.2.6 on 2023-10-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_remove_coach_team_remove_manager_team_team_coach_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('team', models.ManyToManyField(related_name='tournaments', to='tournament.team')),
            ],
        ),
    ]