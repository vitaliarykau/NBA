from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView, CreateView,\
                                        UpdateView, DeleteView

from .models import Player, Team, Match, Stat, Arena
from .forms import MatchForm, StatForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

class TeamsMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all().order_by('city')
        return context


class IndexView(ListView):
    #model = Team
    template_name = 'statistic/page.html'
    context_object_name = 'teams'
    queryset = Team.objects.order_by('city')


class PlayerView(TeamsMixin, DetailView):
    model = Player
    template_name = 'statistic/player_bio.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.get_object()
        context['stats'] = Stat.objects.filter(player=player).order_by('-season')
        return context


class TeamView(TeamsMixin, DetailView):
    model = Team
    template_name = 'statistic/team.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roster'] = Player.objects.filter(team=self.get_object()).order_by('number')
        context['matches'] = Match.objects.filter(Q(team1=self.get_object())|Q(team2=self.get_object())).order_by('-date')
        return context


class PlayersView(TeamsMixin, ListView):
    model = Player
    template_name = 'statistic/players.html'
    context_object_name = 'players'



class TeamsView(TeamsMixin, ListView):
    model = Team
    template_name = 'statistic/teams.html'
    context_object_name = 'teams'


class MatchView(TeamsMixin, DetailView):
    model = Match
    template_name = 'statistic/match.html'
    context_object_name = 'match'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roster1'] = Player.objects.filter(team=self.get_object().team1)
        context['roster2'] = Player.objects.filter(team=self.get_object().team2)
        return context


class MatchesView(TeamsMixin, ListView):
    #model = Match
    template_name = 'statistic/matches.html'
    context_object_name = 'matches'
    queryset = Match.objects.order_by('-date')


class AddMatchView(PermissionRequiredMixin, TeamsMixin, CreateView):
    permission_required = 'statistic.can_moderate'
    login_url = 'users:login'
    model = Match
    form_class = MatchForm
    template_name = 'statistic/new_match.html'
    success_url = reverse_lazy('statistic:matches')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The match was successfully added")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['arenas'] = Arena.objects.all()
        return context


class EditMatchView(PermissionRequiredMixin, TeamsMixin, UpdateView):
    permission_required = ('can_moderate',)
    login_url = 'users:login'
    model = Match
    form_class = MatchForm
    #fields = []
    template_name = 'statistic/edit_match.html'
    success_url = reverse_lazy('statistic:matches')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Data was changed...")
        messages.error(self.request, "Check your data...")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['arenas'] = Arena.objects.all()
        return context



class DeleteMatchView(PermissionRequiredMixin, TeamsMixin, DeleteView):
    permission_required = 'statistic.can_moderate'
    login_url = 'users:login'
    model = Match
    template_name = 'statistic/delete_match.html'
    success_message = "Deleted Successfully"
    success_url = reverse_lazy('statistic:matches')

    def delete(self, request, pk):
        response = super().delete(request)
        messages.success(self.request, "Entry was deleted...")
        return response


class StatView(PermissionRequiredMixin, TeamsMixin, CreateView):
    permission_required = 'statistic.can_moderate'
    login_url = 'users:login'
    model = Stat
    form_class = StatForm
    success_url = reverse_lazy('statistic:matches')
    template_name = 'statistic/stat.html'
    context_object_name = 'stats'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The stats were added")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        context['matches'] = Match.objects.all()
        return context


class SearchView(TeamsMixin, View):
    template_name = 'statistic/search.html'
    homepage = 'statistic/page.html'
    def post(self, request, *args, **kwargs):
        data = request.POST['keyword']
        if data != '':
            result = {}
            result['teams'] = Team.objects.all().order_by('city')
            result['players'] = Player.objects.filter(Q(name__icontains=data) | Q(surname__icontains=data))
            result['teams_found'] = Team.objects.filter(Q(city__icontains=data) | Q(name__icontains=data))
            return render(request, self.template_name, result)
        else:
            return redirect('/')

    def get(self, request, *args, **kwargs):
        return redirect('/')

