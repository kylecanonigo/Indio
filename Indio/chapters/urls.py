from django.urls import path

from chapters.views import ChaptersListView  # Ensure the correct import path here
from chapters.views import LessonsListView  # Ensure the correct import path here

urlpatterns = [
    path('', ChaptersListView.as_view(), name="chapters"),
    path('lessons', LessonsListView.as_view(), name="lessons"),
]

