from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from datetime import date

from movies.models import Movie
data = {
    "movies" : [
        {
        "title": "film adı 1",
        "description" : "film açıklama 1",
        "imageUrl": "m1.jpg",
        "coverImage":"cover1.jpg",
        "slug":"film-adi-1",
        "language":"english",
        "date": date(2021,10,10)
        },
        {
        "title": "film adı 2",
        "description" : "film açıklama 2",
        "imageUrl": "m2.jpg",
        "coverImage":"cover2.jpg",
        "slug":"film-adi-2",
        "language":"english",
        "date": date(2021,5,10)
        },
        {
        "title": "film adı 3",
        "description" : "film açıklama 3",
        "imageUrl": "m3.jpg",
        "coverImage":"cover3.jpg",
        "slug":"film-adi-3",
        "language":"english",
        "date": date(2021,10,5)
        },
        {
        "title": "film adı 4",
        "description" : "film açıklama 4",
        "imageUrl": "m4.jpg",
        "coverImage":"cover1.jpg",
        "slug":"film-adi-4",
        "language":"english",
        "date": date(2021,4,5)
        }
        
        ],
    "sliders":[
        {
            "slider_image":"slider1.jpg",
            "url":"film-adi-1"
        },
        {
            "slider_image":"slider2.jpg",
            "url":"film-adi-2"
        },
        {
            "slider_image":"slider3.jpg",
            "url":"film-adi-3"
        },

        
    ]
}

def index(request):
    movies = Movie.objects.filter(is_active = True, is_home = True)
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "movies":movies,
        "sliders":sliders
    })

def movies(request):
    movies = Movie.objects.filter(is_active = True)
    return render(request, 'movies.html', {
        "movies":movies
    })

def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug = slug)    
    return render(request, 'movie-details.html', {
    'movie':movie,
    'genres':movie.genres.all(),
    'people':movie.people.all(),
    'videos':movie.video_set.all()
    })

# Create your views here.
