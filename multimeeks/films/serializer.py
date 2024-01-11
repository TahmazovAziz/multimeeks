from rest_framework import serializers
from .models import FilmView,Film
from rest_framework.renderers import JSONRenderer

class FilmViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmView
        fields = '__all__'