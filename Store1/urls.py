"""Store1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from posts.views import hello_v
from posts.views import youtube_veiw
from posts.views import google_veiw
from posts.views import now_date
from posts.views import goodbay

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_v),
    path("youtube/", youtube_veiw),
    path('google/', google_veiw),
    path('now_date/', now_date),
    path('goodbay/', goodbay)
]
