from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class users(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    
    def _str_(self):
        return self.username
class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coach=models.ForeignKey(Coach, on_delete=models.CASCADE)
    manager=models.ForeignKey(Manager, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Tournamet_register(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_closed = models.BooleanField(default=False)  

    def check_and_close_registration(self):
        # Check if the number of registered teams for this tournament is 10 or more
        if self.regiterteam_set.count() >= 10:
            self.registration_closed = True
            self.save()
            
    def __str__(self):
        return self.name  

class Regiter_team(models.Model):
    tournament_name = models.ForeignKey(Tournamet_register, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    regiter_date = models.DateField( auto_now_add=True)  
    
    

class Schedule(models.Model):
    tournament = models.ForeignKey(Tournamet_register, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.tournament.name  

class confomed_team(models.Model):
    schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)
    regiter_team=models.ForeignKey(Regiter_team, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.regiter_team.team.name 

class Match(models.Model):
    tournament = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    team1 = models.ForeignKey(confomed_team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(confomed_team, on_delete=models.CASCADE, related_name='team2_matches')
    match_date = models.DateTimeField()
    location = models.CharField(max_length=100)

@receiver(post_save, sender=Tournamet_register)
def create_schedule_on_registration_closed(sender, instance, **kwargs):
    if instance.registration_closed:
        # Create a schedule for the tournament
        schedule = Schedule.objects.create(tournament=instance)

        # Fetch all teams registered for this tournament
        registered_teams = Regiter_team.objects.filter(tournament_name=instance)

        # Loop through the registered teams and add them to the ConfirmedTeam table
        for reg_team in registered_teams:
            confomed_team.objects.create(
                regiter_team=reg_team,
                schedule=schedule,
            )

            



