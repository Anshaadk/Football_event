# Generated by Django 4.2.6 on 2023-10-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0008_venue_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='scheduling_in_progress',
            field=models.BooleanField(default=False),
        ),
    ]