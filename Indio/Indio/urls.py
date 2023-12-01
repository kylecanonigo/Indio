"""
URL configuration for Indio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from timeline.views import TimelineTypeGameView
from website.views import index, about, login
from four.views import FourPicsOneWordGameView
from matching.views import MatchingTypeGameView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('four/', FourPicsOneWordGameView.as_view(), name="four"),
    path('matching/', MatchingTypeGameView.as_view(), name="matching"),
    path('timeline/', TimelineTypeGameView.as_view(), name="timeline"),
    path('login/', login, name="login"),
    path('chapters/', include('chapters.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

