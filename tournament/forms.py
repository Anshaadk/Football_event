from django import forms
from .models import *
from django.forms.widgets import DateInput




class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs and assign it to 'user' variable
        super(TeamRegistrationForm, self).__init__(*args, **kwargs)

        if user is not None:
            # Filter the queryset for coach and manager based on the logged-in user
            self.fields['coach'].queryset = Coach.objects.filter(user=user)
            self.fields['manager'].queryset = Manager.objects.filter(user=user)
class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'  # Include all fields from the TeamMember model

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'  # Include all fields from the Coach model

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'  # Include all fields from the Manager model

class TournametRegisterForm(forms.ModelForm):
    class Meta:
        model = Tournamet_register
        fields = '__all__'
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class RegiterTeamForm(forms.ModelForm):
    class Meta:
        model = Regiter_team
        fields = ['tournament_name', 'team']
        
        
    
class MatchCreationForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'
        widgets = {
            'match_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, schedule_id=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter the queryset for team1 and team2 based on the schedule
        if schedule_id is not None:
            schedule = Schedule.objects.get(pk=schedule_id)
            registered_teams = schedule.confomed_team_set.all()
            self.fields['team1'].queryset = registered_teams
            self.fields['team2'].queryset = registered_teams
            
class EditMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = [ 'match_date', 'location', 'status', 'score']
        widgets = {
            'match_date': forms.DateInput(attrs={'type': 'date'}),
        }