from django.urls import path

from .views import (
    home,
    myPage,
    tournament,
    league,
    about,
    registerPage,
    loginPage,
    logoutUser,
    leagueView,
    tournamentView,
)


urlpatterns = [
    path('', home),
    path('mypage/',myPage),
    path('tournament/', tournament),
    path('tournament/<str:pk>/', tournamentView, name="tournamentview"),
    path('league/', league),
    path('league/<str:pk>/', leagueView, name="leagueview"),
    path('about/', about),
    path('register/', registerPage),
    path('login/', loginPage),
    path('logout/', logoutUser),

]