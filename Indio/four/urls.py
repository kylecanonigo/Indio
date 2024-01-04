from django.urls import path

from four.views import CongratsView, FourPicsOneWordGameView  # Ensure the correct import path here
app_name = 'four'
urlpatterns = [
    path('<int:chapter_id>', FourPicsOneWordGameView.as_view(), name="four"),
    path('congrats', CongratsView.as_view(), name="congrats")
]

