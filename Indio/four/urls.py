from django.urls import path

from four.views import CongratsView, FourPicsOneWordGameView  # Ensure the correct import path here

urlpatterns = [
    path('', FourPicsOneWordGameView.as_view(), name="four"),
    path('congrats', CongratsView.as_view(), name="congrats")
]

