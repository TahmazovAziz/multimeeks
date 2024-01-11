from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from films.views import FilmViewAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/film' , FilmViewAPIView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('film/', include('films.urls')),
    path('', include(router.urls))
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)