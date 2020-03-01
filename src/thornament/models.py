from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tournament(models.Model):
    TYPE = (
        ('Single Elemenation', 'Single Elemenation'),
        ('Double Elemenation', 'Double Elemenation'),
        ('Round Robin', 'Round Robin')
        )

    tournament_name     = models.CharField(max_length=200, null=True)
    tournament_type     = models.CharField(max_length=200, null=True, choices=TYPE)
    tournament_teams    = models.IntegerField(null=True)
    tournament_seed     = models.BooleanField(default=False, null=True)
    date_created        = models.DateTimeField(auto_now_add=True, null=True)
    owner               = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.tournament_name


class League(models.Model):
    TYPE = (
        ('One time', 'One time'),
        ('Two times', 'Two times'),
        ('Three times', 'Three times')
        )

    league_name     = models.CharField(max_length=200, null=True)
    league_type     = models.CharField(max_length=200, null=True, choices=TYPE)
    league_teams    = models.IntegerField(null=True)
    league_seed     = models.BooleanField(default=False, null=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True)
    owner           = models.ForeignKey(User, null=True , on_delete= models.SET_NULL)

    def __str__(self):
        return self.league_name

    
class LeagueParticipant(models.Model):
    participant_name    = models.CharField(max_length=200, null=True),
    participant_win     = models.IntegerField(null=True),
    participant_loss    = models.IntegerField(null=True),
    participant_ot      = models.IntegerField(null=True),
    Participant_point   = models.IntegerField(null=True),
    owner               = models.ForeignKey(League, null=True , on_delete= models.SET_NULL)

    def __str__(self):
        return self.participant_name


class TournamentParticipant(models.Model):
    participant_name    = models.CharField(max_length=200, null=True),
    participant_win     = models.IntegerField(null=True),
    participant_loss    = models.IntegerField(null=True),
    participant_ot      = models.IntegerField(null=True),
    Participant_point   = models.IntegerField(null=True),
    owner               = models.ForeignKey(Tournament, null=True , on_delete= models.SET_NULL)

    def __str__(self):
        return self.participant_name