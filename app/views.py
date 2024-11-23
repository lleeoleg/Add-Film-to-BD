from django.shortcuts import render
from .models import Movie


def create_movie(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        genre = request.POST['genre']
        description = request.POST['description']
        duration = request.POST['duration']
        Movie.objects.create(name=name, genre=genre, year=int(year), description=description, duration=duration)        
    else:
        print('GET')
    return render(request, 'create_movie.html')