from django.db import models
from django.core.validators import FileExtensionValidator
class Film(models.Model):
    source = models.FileField(upload_to="video/%y" ,null=True,  
                           blank=True,  
                           validators=[FileExtensionValidator( ['mp4'] ) ])    
class FilmView(models.Model):
    poster = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True , null=True)
    length = models.DurationField()
    name = models.CharField(max_length=200, default='.')
    source = models.ForeignKey('Film' ,  on_delete=models.CASCADE)
