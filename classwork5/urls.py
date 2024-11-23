from django.contrib import admin
from django.urls import path
from app.views import create_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_movie)
]
