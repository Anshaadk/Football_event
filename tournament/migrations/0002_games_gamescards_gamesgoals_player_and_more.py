# Generated by Django 4.2.5 on 2023-10-04 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rival_team', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('goals_against', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='GamesCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('yellow', 'yellow'), ('red', 'red')], max_length=6)),
                ('minute', models.IntegerField(default=0, max_length=3)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.games')),
            ],
            options={
                'verbose_name_plural': 'Games Cards',
            },
        ),
        migrations.CreateModel(
            name='GamesGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=255)),
                ('minute', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.games')),
            ],
            options={
                'verbose_name_plural': 'Games Goals',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='manager',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.RenameModel(
            old_name='Team',
            new_name='Position',
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.position'),
        ),
        migrations.AddField(
            model_name='gamesgoals',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.player'),
        ),
        migrations.AddField(
            model_name='gamescards',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.player'),
        ),
    ]
