from django.shortcuts import render

from ex01.models import *

def populate(request):
    results = []
    films = [
        Movies(episode_nb=1, title='The Phantom Menace', director='George Lucas',
            producer='Rick McCallum', release_date='1999-05-19'),
        Movies(episode_nb=2, title='Attack of the Clones', director='George Lucas',
            producer='Rick McCallum', release_date='2002-05-16'),
        Movies(episode_nb=3, title='Revenge of the Sith', director='George Lucas',
            producer='Rick McCallum', release_date='2005-05-19'),
        Movies(episode_nb=4, title='A New Hope', director='George Lucas',
            producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25'),
        Movies(episode_nb=5, title='The Empire Strikes Back', director='Irvin Kershner',
            producer='Gary Kutz, Rick McCallum', release_date='1980-05-17'),
        Movies(episode_nb=6, title='Return of the Jedi', director='Richard Marquand',
            producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25'),
        Movies(episode_nb=7, title='The Force Awakens', director='J. J. Abrams',
            producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11'),
    ]
    for film in films:
        try:
            film.save()
            results.append('OK')
        except Exception as e:
            results.append(str(e))
    return render(request, 'ex05/populate.html', {"results": results})

def display(request):
    result = 'No data available'
    films = []
    films = Movies.objects.all()
    headers = ['episode_nb','title','director', 'producer', 'release_date', 'opening_crawl']
    return render(request, 'ex05/display.html', {"films": films, "result": result, "headers": headers})


def remove(request):
    titles = []
    result = ''
    try:
        if request.method == "POST":
            value = request.POST.get('movies')
            movie = Movies.objects.get(title=value)
            movie.delete()
        titles = Movies.objects.values_list('title', flat=True)
        result = "No data available"
        
    except Exception:
        result = "No data available"
    return render(request, 'ex05/remove.html', {"result": result, "titles": titles})
   