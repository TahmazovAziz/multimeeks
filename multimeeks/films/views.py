from rest_framework import generics
from .models import FilmView,Film
from .serializer import FilmViewSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.forms import model_to_dict
from django.utils.dateparse import parse_duration

class FilmViewAPIView(viewsets.ModelViewSet):
  queryset = FilmView.objects.all()
  serializer_class = FilmViewSerializer
  



# class FilmViewAPIView(generics.ListAPIView):
#     queryset = FilmView.objects.all()
#     serializer_class = FilmViewSerializer