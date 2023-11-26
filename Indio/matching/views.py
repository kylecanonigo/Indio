from django.shortcuts import render, get_object_or_404
from django.views import View

from matching.models import MatchingTypeGame


# Create your views here.


def matching(request):
    return render(request, "matching/matching.html")
#
# class MatchingTypeGameView(View):
#     template_name = 'matching/matching.html'  # Replace with your actual template name
#     max_attempts = 3  # Set the maximum number of attempts
#
#     def get(self, request, game_id):
#         game = get_object_or_404(MatchingTypeGame, pk=game_id)
#
#         # Retrieve the attempts count from the session or set to 0 if not present
#         attempts = request.session.get('attempts_matching', 0)
#
#         # Basic logic for the game (replace with your specific game logic)
#         submitted_answers = {
#             'answer1': request.GET.get('answer1', ''),
#             'answer2': request.GET.get('answer2', ''),
#             'answer3': request.GET.get('answer3', ''),
#             # Assuming answers are passed in the URL for the matching game
#         }
#
#         if attempts >= self.max_attempts:
#             result_message = f"Max attempts reached. Try again later."
#         else:
#             # Implement logic to check submitted answers against correct answers
#             # For example, check if submitted_answers['answer1'] matches game.correct_answer1
#
#             # Example: if correct_answers['answer1'] == submitted_answers['answer1'] and so on
#             # Set the appropriate result_message based on correctness
#
#         # Update the attempts count in the session
#         request.session['attempts_matching'] = attempts
#
#         # Passing game details, result message, and attempts to the template
#         context = {
#             'game': game,
#             'result_message': result_message,
#             'attempts': attempts,
#             'max_attempts': self.max_attempts,
#             # Add additional context data as needed for your game logic
#         }
#
#         return render(request, self.template_name, context)
