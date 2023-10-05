# Generated by Django 4.2.5 on 2023-10-04 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_games_gamescards_gamesgoals_player_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='gamescards',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gamescards',
            name='player',
        ),
        migrations.RemoveField(
            model_name='gamesgoals',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gamesgoals',
            name='player',
        ),
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
        migrations.RenameModel(
            old_name='Position',
            new_name='Team',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
        migrations.DeleteModel(
            name='GamesCards',
        ),
        migrations.DeleteModel(
            name='GamesGoals',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team'),
        ),
        migrations.AddField(
            model_name='manager',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team'),
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team'),
        ),
    ]