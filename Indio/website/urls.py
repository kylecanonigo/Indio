from django.urls import path

from . import views
app_name = 'website'
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('', views.About.as_view(), name='about'),
]
