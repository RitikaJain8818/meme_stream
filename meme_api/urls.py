from django.urls import path
from meme_api import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('memes', views.memes),
    path('memes/<int:pk>', views.memeDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)