from django.contrib import admin

# Register your models here.

from .models import Tournament, League, LeagueParticipant, TournamentParticipant

admin.site.register(Tournament)
admin.site.register(League)
admin.site.register(LeagueParticipant)
admin.site.register(TournamentParticipant)