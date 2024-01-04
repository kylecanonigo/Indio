import os

import openai
from django.shortcuts import render
from django.views import View
import random

from openai import OpenAI

from four.models import GameWords




# Create your views here.

client = OpenAI()


class FourPicsOneWordGameView(View):
    template_name = 'four/four.html'
    congrats_template = 'congrats'
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def get(self, request, chapter_id):
        current_game, next_game_index, correct_answer_buttons, total_games = self._get_game_details(request, chapter_id)

        image_url_1 = "https://www.w3schools.com/images/lamp.jpg"      #self._fetch_image_1()
        image_url_2 = "https://www.w3schools.com/images/lamp.jpg"     #self._fetch_image_2()

        context = {
            'current_game': current_game,
            'next_game_index': next_game_index,
            'correct_answer_buttons': correct_answer_buttons,
            'total_games': total_games,
            'image_url_1': image_url_1,
            'image_url_2': image_url_2,
            'chapter_id': chapter_id,
        }
        return render(request, self.template_name, context)

    def _fetch_image_1(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = client.images.generate(
            model="dall-e-2",
            prompt="pop art of government",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        print(image_url)
        return image_url

    def _fetch_image_2(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = client.images.generate(
            model="dall-e-2",
            prompt="post impressionism of government",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        print(image_url)
        return image_url

    def setSession(self, request,  word_ids):
        if ('word_ids' in request.session) and ('word_index' in request.session):
            return

        request.session['word_ids'] = word_ids
        request.session['word_index'] = 0


    def _get_game_details(self, request, chapter_id):
        queryset = GameWords.objects.filter(chapter_id_id=chapter_id, is_ans=False)

        if not queryset:
            print("Empty")
            return None, None, None, 0

        word_ids = list(queryset.values_list('word_id', flat=True))
        random.shuffle(word_ids)

        self.setSession(request, word_ids)

        game_index = self.getIndex(request)
        current_game = self.getCurrentQuestion(game_index, queryset)
        total_games = len(queryset)
        next_game_index = self.NextIndex(request)
        correct_answer_buttons = self._prepare_correct_answer_buttons(current_game)
        return current_game, next_game_index, correct_answer_buttons, total_games

    def getCurrentQuestion(self, index, queryset):
        if index is None:
            return queryset[0]
        return queryset[index]

    def getIndex(self, request):
        curr = request.session.get('word_index', -1)
        return curr


    def NextIndex(self, request):
        curr = request.session.get('word_index', -1)
        request.session['word_index'] = curr + 1
        return curr + 1

    def _prepare_correct_answer_buttons(self, current_game):
        correct_answer_buttons = []
        for char in current_game.word:
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
