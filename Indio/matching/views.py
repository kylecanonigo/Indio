from django.shortcuts import render, get_object_or_404
from django.views import View

from matching.models import MatchingTypeGame

from django.shortcuts import render, get_object_or_404
import random

# Create your views here.


class MatchingTypeGameView(View):
    template_name = 'matching/matching.html'

    def get(self, request):
        current_game, next_game_index = self._get_game_details(request)
        context = {
            'current_game': current_game,
            'next_game_index': next_game_index,
            'correct_img1': current_game.correct_img1.url,
            'correct_img2': current_game.correct_img2.url,
        }
        return render(request, self.template_name, context)

    def _get_game_details(self, request):
        games = MatchingTypeGame.objects.all()
        game_index = int(request.GET.get('game_index', 0))
        current_game = self._get_current_game(games, game_index)
        next_game_index = self._calculate_next_game_index(game_index, len(games))
        return current_game, next_game_index

    def _get_current_game(self, games, game_index):
        return games[game_index]

    def _calculate_next_game_index(self, game_index, total_games):
        return (game_index + 1) % total_games