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
    path('tournament/<str:pk>/', tournamentView),
    path('league/', league),
    path('league/<str:pk>/', leagueView),
    path('about/', about),
    path('register/', registerPage),
    path('login/', loginPage),
    path('logout/', logoutUser),

]