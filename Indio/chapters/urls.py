from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('', views.chapters_list, name="chapters"),
    path('lessons', views.lessons_list, name="lessons")
]

