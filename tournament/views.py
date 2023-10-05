# tournament/views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic import *
from datetime import timedelta,datetime
from django.utils import timezone
from django.db.models import Q
from itertools import combinations
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy



def register_team(request):
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Create a success template and URL
    else:
        form = TeamRegistrationForm(user=request.user)  # Pass the logged-in user to the form
    
    return render(request, './register_team.html', {'form': form})



def edit_team(request, team_id):
    # Fetch the team to be edited or return a 404 error if it doesn't exist
    team = get_object_or_404(Team, pk=team_id)
    
    # Check if the logged-in user has permission to edit the team
    if request.user != team.user:
        return HttpResponseForbidden("You don't have permission to edit this team.")
    
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST, instance=team, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the desired page after editing
    else:
        form = TeamRegistrationForm(instance=team, user=request.user)
    
    return render(request, './user/edit_team.html', {'form': form, 'team': team})

def register_coach(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Create a success template and URL
    else:
        form = CoachForm()
    
    return render(request, './register_coach.html', {'form': form})


def register_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Create a success template and URL
    else:
        form = ManagerForm()
    
    return render(request, './register_manager.html', {'form': form})

def registration_success(request):
    return render(request, './registration_success.html')


def home(request):
    return render(request,'home.html')

def admin_home(request):
    teams = Team.objects.all()  # Retrieve all teams from the database
    context = {'teams': teams}
    return render(request,'./admin_home.html',context)

def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = TeamMember.objects.filter(team=team)  # Use filter to get all players
    context = {'team': team, 'players': players}
    return render(request, 'team_detail.html', context)



def register_team_member(request, pk):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            # Save the form data and associate it with the team
            team_member = form.save(commit=False)
            team_member.team_id = pk  # Associate the team member with the team based on pk
            team_member.save()

            # Redirect to the team detail page for the specified team
            return redirect(reverse('team_detail', args=[pk]))  # Assuming you have a 'team_detail' URL pattern

    else:
        form = TeamMemberForm()
    
    return render(request, 'register_team_member.html', {'form': form})

def edit_team_member(request, team_member_id):
    team_member = get_object_or_404(TeamMember, pk=team_member_id)
    
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            return redirect(reverse('team_detail', args=[team_member.team.pk]))  # Redirect to the team detail page
    else:
        form = TeamMemberForm(instance=team_member)
    
    return render(request, 'edit_team_member.html', {'form': form, 'team_member': team_member})

def delete_team_member(request, team_member_id):
    team_member = get_object_or_404(TeamMember, pk=team_member_id)
    if team_member:
        team_member.delete()
    return redirect(reverse('team_detail', args=[team_member.team.pk]))  # Redirect to the team detail page

def TournametRegisterListView(request):
    tournaments = Tournamet_register.objects.all()

    context = {
        'tournaments': tournaments,
    }

    return render(request, 'tournament_register_list.html', context)

class TournametRegisterCreateView(CreateView):
    model = Tournamet_register
    form_class = TournametRegisterForm
    template_name = 'tournament_register_form.html'
    success_url = reverse_lazy('tournament_register_list')

class TournametRegisterUpdateView(UpdateView):
    model = Tournamet_register
    form_class = TournametRegisterForm
    template_name = 'tournament_register_form.html'
    success_url = reverse_lazy('tournament_register_list')

class TournametRegisterDeleteView(DeleteView):
    model = Tournamet_register
    template_name = 'tournament_register_confirm_delete.html'
    success_url = reverse_lazy('tournament_register_list')

class RegiterTeamListView(ListView):
    model = Regiter_team
    template_name = 'register_team_list.html'
    context_object_name = 'register_teams'

class RegiterTeamCreateView(CreateView):
    model = Regiter_team
    form_class = RegiterTeamForm
    template_name = 'register_team_form.html'
    success_url = reverse_lazy('register_team_list')

class RegiterTeamUpdateView(UpdateView):
    model = Regiter_team
    form_class = RegiterTeamForm
    template_name = 'register_team_form.html'
    success_url = reverse_lazy('register_team_list')

class RegiterTeamDeleteView(DeleteView):
    model = Regiter_team
    template_name = 'register_team_confirm_delete.html'
    success_url = reverse_lazy('register_team_list')


def registered_teams_for_tournament(request, tournament_id):
    tournament = Tournamet_register.objects.get(pk=tournament_id)
    registered_teams = Regiter_team.objects.filter(tournament_name=tournament)
    
    return render(request, './user/registered_teams.html', {'tournament': tournament, 'registered_teams': registered_teams})

    

def TournametListing(request):
    
    model = Tournamet_register.objects.all()
    context={
        'tournaments':model,
    }
    return render(request,'user/List_tout.html',context)

def reg_player_list(request,id):
    print(id)
    mem = TeamMember.objects.filter(team=id)
    
    print(mem)
    context={
        'players':mem,
    }

    return render(request,'user/playerlist.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user =auth.authenticate(username=user_name,password=pass_word) 
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            messages.info(request,'invalid some thing')
            return redirect(login)
    return render(request, 'login.html')


def register(request):

    if request.method == 'POST':

        user_name=request.POST['username']
        emails=request.POST['email']
        pass_word=request.POST['password']
        confirm_password = request.POST['confirm_password']
        if pass_word==confirm_password:
            if User.objects.filter(email=emails).exists():
                messages.info(request,'Email is exist')
                return redirect(register)
            else:
                if User.objects.filter(username=user_name).exists():
                    messages.info(request, 'username is exist')
                    return redirect(register)
                else:
                    user = User.objects.create_user(username=user_name,password=pass_word,email=emails)
                    user.set_password(pass_word)
                    user.save()
                    print('success')
                    return redirect(login)
        else:
            return redirect(register)
                
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect(login)
    
def user_home(request):
    return render(request,'user/userbase.html')

def user_profile(request):
    user=request.user
    print(user)
    teams = Team.objects.filter(user=user) 
    print(teams)# Retrieve all teams from the database
    context = {'teams': teams}
    return render(request,'user/profile.html',context)


def view_schedule(request):
    schedules = Schedule.objects.all()
    context = {
        'schedules': schedules,
    }
    return render(request, 'view_schedule.html', context)

def create_matches(request, schedule_id):
    # Retrieve the schedule based on schedule_id
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.method == 'POST':
        form = MatchCreationForm(request.POST, schedule_id=schedule_id)
        if form.is_valid():
            # Set the tournament and match date based on the schedule
            match = form.save(commit=False)
            match.tournament = schedule
            match.save()
            return redirect('view_schedule')  # Redirect to the match list or another page
    else:
        form = MatchCreationForm(schedule_id=schedule_id)

    context = {
        'form': form,
        'schedule': schedule,  # Pass the schedule to the template
    }

    return render(request, 'create_matches.html', context)

class MatchListView(ListView):
    model = Match
    template_name = 'match_list.html'
    context_object_name = 'matches'

    def get_queryset(self):
        # Retrieve the schedule based on the schedule_id URL parameter
        schedule_id = self.kwargs.get('schedule_id')
        schedule = get_object_or_404(Schedule, pk=schedule_id)

        # Filter matches by the selected schedule
        return Match.objects.filter(tournament__id=schedule.id)
    
    
def edit_match(request, pk):
    match = get_object_or_404(Match, pk=pk)

    if request.method == 'POST':
        form = EditMatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_list', schedule_id=match.tournament.id)
    else:
        form = EditMatchForm(instance=match)

    context = {
        'form': form,
        'match': match,
    }

    return render(request, 'edit_match.html', context)