from django.urls import path

from four.views import CongratsView, FourPicsOneWordGameView, updateRecord  # Ensure the correct import path here
app_name = 'four'
urlpatterns = [
    path('<int:chapter_id>', FourPicsOneWordGameView.as_view(), name="four"),
    path('congrats', CongratsView.as_view(), name="congrats"),
    path('update/<int:word_id>/', updateRecord.as_view(), name="update")
]

