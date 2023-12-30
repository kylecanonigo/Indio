from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
import random
from four.models import FourPicsOneWord

import base64
import os
import openai
from openai import OpenAI

# Create your views here.

client = OpenAI()


class FourPicsOneWordGameView(View):
    template_name = 'four/four.html'
    congrats_template = 'congrats'
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def get(self, request):
        current_game, next_game_index, correct_answer_buttons, total_games = self._get_game_details(request)

        # image_url_1 = self._fetch_image_1()
        # image_url_2 = self._fetch_image_2()

        context = {
            'current_game': current_game,
            'next_game_index': next_game_index,
            'correct_answer_buttons': correct_answer_buttons,
            'total_games': total_games,
            # 'image_url_1': image_url_1,
            # 'image_url_2': image_url_2,
        }
        return render(request, self.template_name, context)

    # def _fetch_image_1(self):
    #     openai.api_key = os.getenv("OPENAI_API_KEY")
    #     response = client.images.generate(
    #         model="dall-e-2",
    #         prompt="pop art of government",
    #         size="1024x1024",
    #         quality="standard",
    #         n=1,
    #     )
    #
    #     image_url = response.data[0].url
    #     print(image_url)
    #     return image_url
    #
    # def _fetch_image_2(self):
    #     openai.api_key = os.getenv("OPENAI_API_KEY")
    #     response = client.images.generate(
    #         model="dall-e-2",
    #         prompt="post impressionism of government",
    #         size="1024x1024",
    #         quality="standard",
    #         n=1,
    #     )
    #
    #     image_url = response.data[0].url
    #     print(image_url)
    #     return image_url

    def _get_game_details(self, request):
        games = FourPicsOneWord.objects.all()
        game_index = int(request.GET.get('game_index', 0))
        current_game = self._get_current_game(games, game_index)
        total_games = len(games)
        next_game_index = self._calculate_next_game_index(game_index, total_games)
        correct_answer_buttons = self._prepare_correct_answer_buttons(current_game)
        return current_game, next_game_index, correct_answer_buttons, total_games

    def _get_current_game(self, games, game_index):
        return games[game_index]

    def _calculate_next_game_index(self, game_index, total_games):
        return game_index + 1

    def _prepare_correct_answer_buttons(self, current_game):
        correct_answer_buttons = []
        for char in current_game.correct_answer:
            if char == ' ':
                correct_answer_buttons.append('')
            else:
                correct_answer_buttons.append(char)
        random.shuffle(correct_answer_buttons)
        return correct_answer_buttons


class CongratsView(View):
    template_name = 'four/congrats.html'

    def get(self, request):
        return render(request, self.template_name)
