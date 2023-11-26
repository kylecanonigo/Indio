from django.shortcuts import render, get_object_or_404
from django.views import View

from four.models import FourPicsOneWord


# Create your views here.


def four(request):
    return render(request, "four/four.html")
#
# class FourPicsOneWordGameView(View):
#     template_name = 'four/four.html'  # Replace with your actual template name
#     max_attempts = 3  # Set the maximum number of attempts
#
#     def get(self, request, game_id):
#         game = get_object_or_404(FourPicsOneWord, pk=game_id)
#
#         # Retrieve the attempts count from the session or set to 0 if not present
#         attempts = request.session.get('attempts', 0)
#
#         # Basic logic for the game (replace with your specific game logic)
#         submitted_answer = request.GET.get('answer', '')  # Assuming answer is passed in the URL
#
#         if attempts >= self.max_attempts:
#             result_message = f"Max attempts reached. The answer is {game.correct_answer}."
#         else:
#             if submitted_answer.lower() == game.correct_answer.lower():
#                 result_message = 'Correct!'
#             else:
#                 result_message = 'Incorrect. Try again!'
#                 attempts += 1
#
#         # Update the attempts count in the session
#         request.session['attempts'] = attempts
#
#         # Passing game details and result message to the template
#         context = {
#             'game': game,
#             'result_message': result_message,
#             'attempts': attempts,
#             'max_attempts': self.max_attempts,
#             # Add additional context data as needed for your game logic
#         }
#
#         return render(request, self.template_name, context)


