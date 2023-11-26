from django.shortcuts import render, get_object_or_404
from django.views import View

from timeline.models import TimelineTypeGame


# Create your views here.


def timeline(request):
    return render(request, "timeline/timeline.html")


# class TimelineTypeGameView(View):
#     template_name = 'timeline_game.html'  # Replace with your actual template name
#
#     def get(self, request, game_id):
#         game = get_object_or_404(TimelineTypeGame, pk=game_id)
#
#         # Mocking logic for the game (replace this with your actual game logic)
#         submitted_answers = {
#             'submitted_img1': request.GET.get('submitted_img1'),
#             'submitted_img2': request.GET.get('submitted_img2'),
#             'submitted_img3': request.GET.get('submitted_img3')
#         }
#
#         correct_answers = {
#             'correct_img1': str(game.correct_img1),
#             'correct_img2': str(game.correct_img2),
#             'correct_img3': str(game.correct_img3)
#         }
#
#         # Check if the submitted answers match the correct answers
#         result = all(submitted_answers[key] == value for key, value in correct_answers.items())
#
#         result_message = 'Correct!' if result else 'Incorrect. Try again!'
#
#         # Passing game details and result message to the template
#         context = {
#             'game': game,
#             'result_message': result_message,
#             # Add additional context data as needed for your game logic
#         }
#
#         return render(request, self.template_name, context)

