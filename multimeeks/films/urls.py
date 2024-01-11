from django.urls import path
from main.views import FilmViewDetailView

urlpatterns = [
    path('<int:pk>', FilmViewDetailView.as_view(), name="film")
]
