from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import CreateUserForm
from .models import *

# Create your views here.

def home(request):
    tournaments = Tournament.objects.all()
    leagues = League.objects.all()

    context = {
        'tournaments':tournaments, 
        'leagues':leagues,
    }

    if request.user.is_authenticated:
        return redirect('/mypage')    
    return render(request, 'thornament/home.html', context)


@login_required(login_url='/login')
def myPage(request):
    return render(request, 'thornament/mypage.html')

@login_required(login_url='/login')
def tournament(request):
    tournaments = Tournament.objects.all()

    context = {
        'tournaments':tournaments
    }

    return render(request, 'thornament/tournament.html', context)

@login_required(login_url='/login')
def league(request):
    leagues = League.objects.all()

    context = {
        'leagues':leagues,
    }

    return render(request, 'thornament/league.html', context)


def leagueView(request, pk):
    league = League.objects.get(id=pk)

    participants = league.leagueparticipant_set.all()

    context = {
        'league':league,
        'participants':participants,
    }
    return render(request, 'thornament/league_view.html', context)


def tournamentView(request, pk):
    tournament = Tournament.objects.get(id=pk)

    participants = tournament.tournamentparticipant_set.all()

    context = {
        'tournament':tournament,
        'participants':participants,
    }
    return render(request, 'thornament/tournament_view.html', context)


def about(request):
    return render(request, 'thornament/about.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account ' + user + ' was created please login')

                return redirect('/login')

        context = {'form': form}
        return render(request, 'thornament/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid username or password!')

        context = {}
        return render(request, 'thornament/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')