
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'statistic'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('team<int:pk>/', views.TeamView.as_view(), name='team'),
    path('players/', views.PlayersView.as_view(), name='players'),
    path('teams/', views.TeamsView.as_view(), name='teams'),
    path('players/player<int:pk>/', views.PlayerView.as_view(), name='player_bio'),
    path('matches/', views.MatchesView.as_view(), name='matches'),
    path('matches/match<int:pk>', views.MatchView.as_view(), name='match'),
    path('matches/new_match/', views.AddMatchView.as_view(), name='new_match'),
    path('matches/edit_match/<int:pk>/', views.EditMatchView.as_view(), name='edit_match'),
    path('matches/delete_match/match<int:pk>/', views.DeleteMatchView.as_view(), name='delete_match'),
    path('stat/', views.StatView.as_view(), name='add_stat'),
    path('search/', views.SearchView.as_view(), name='search'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

