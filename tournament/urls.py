# tournament/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('admin_side/',admin_home,name='admin_home'),
    path('register/team/', register_team, name='register_team'),
    path('register/team-member/<int:pk>/', register_team_member, name='register_team_member'),
    path('register/coach/', register_coach, name='register_coach'),
    path('register/manager/', register_manager, name='register_manager'),
    path('registration-success/', registration_success, name='registration_success'), 
    path('team/<int:team_id>/', team_detail, name='team_detail'),
    path('edit_team/<int:team_id>/', edit_team, name='edit_team'),
    path('team/edit/<int:team_member_id>/', edit_team_member, name='edit_team_member'),
    path('team/delete/<int:team_member_id>/', delete_team_member, name='delete_team_member'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path ('user_home/',user_home,name='user_home'),
    path ('user_profile/',user_profile,name='user_profile'),
    path('tournaments/', TournametRegisterListView, name='tournament_register_list'),
    path('tournaments/create/', TournametRegisterCreateView.as_view(), name='tournament_register_create'),
    path('tournaments/<int:pk>/update/', TournametRegisterUpdateView.as_view(), name='tournament_register_update'),
    path('tournaments/<int:pk>/delete/', TournametRegisterDeleteView.as_view(), name='tournament_register_delete'),
    path('tournament/<int:tournament_id>/registered_teams/',registered_teams_for_tournament, name='registered_teams_for_tournament'),
    path('register_teams/',RegiterTeamListView.as_view(), name='register_team_list'),
    path('register_teams/create/', RegiterTeamCreateView.as_view(), name='register_team_create'),
    path('register_teams/<int:pk>/update/', RegiterTeamUpdateView.as_view(), name='register_team_update'),
    path('register_teams/<int:pk>/delete/', RegiterTeamDeleteView.as_view(), name='register_team_delete'),
    path('list_tournamet/',TournametListing, name='tournament_listing'),
    path('playerliting/<int:id>/',reg_player_list,name='playerlist'),
    path('view_schedule/',view_schedule, name='view_schedule'),
    path('create-matches/<int:schedule_id>/',create_matches, name='create_matches'),
    path('matches/<int:schedule_id>/', MatchListView.as_view(), name='match_list'),
    path('matches/<int:pk>/edit/', edit_match, name='edit_match'),
    
]