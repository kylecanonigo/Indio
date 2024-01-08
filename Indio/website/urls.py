from django.urls import path

from . import views
app_name = 'website'
urlpatterns = [
    path('index/', views.Index.as_view(), name="index"),
    path('', views.Home.as_view(), name='home'),
]

