from django.shortcuts import render
from films.models import FilmView
from films.models import Film, FilmView
from django.views import View
from django.views.generic.detail import DetailView


def home(request):
    film_view = FilmView.objects.all()
    return render(request, 'main/home.html',{"film_view":film_view})


class FilmViewDetailView(DetailView):
    model = FilmView
    template_name = 'film/video.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foreign_key = self.object.source
        context['foreign_key'] = foreign_key
        return context
    
    