
from django.shortcuts import render, get_object_or_404
from django.views import View
import random
from four.models import FourPicsOneWord

# Create your views here.


class FourPicsOneWordGameView(View):
    template_name = 'four/four.html'

    def get(self, request):
        current_game, next_game_index, correct_answer_buttons = self._get_game_details(request)
        context = {
            'current_game': current_game,
            'next_game_index': next_game_index,
            'correct_answer_buttons': correct_answer_buttons,
        }
        return render(request, self.template_name, context)

    def _get_game_details(self, request):
        games = FourPicsOneWord.objects.all()
        game_index = int(request.GET.get('game_index', 0))
        current_game = self._get_current_game(games, game_index)
        next_game_index = self._calculate_next_game_index(game_index, len(games))
        correct_answer_buttons = self._prepare_correct_answer_buttons(current_game)
        return current_game, next_game_index, correct_answer_buttons

    def _get_current_game(self, games, game_index):
        return games[game_index]

    def _calculate_next_game_index(self, game_index, total_games):
        return (game_index + 1) % total_games

    def _prepare_correct_answer_buttons(self, current_game):
        correct_answer_buttons = []
        for char in current_game.correct_answer:
            if char == ' ':
                correct_answer_buttons.append('')
            else:
                correct_answer_buttons.append(char)
        random.shuffle(correct_answer_buttons)
        return correct_answer_buttons
