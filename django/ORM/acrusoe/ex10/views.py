from django.shortcuts import render

from ex10.models import *
import datetime
import json

def index(request):
    results = ['']
    planets, people, movies, planet = [], [], [], []
    colonnes_planets = ['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']
    colonnes_people = ['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld']
    with open('ex10/ex10_initial_data.json', 'r') as f:
        test = json.load(f)
        planets = [planet for planet in test if planet['model'] == 'ex10.planets']
        people = [item for item in test if item['model'] == 'ex10.people']
        movies = [item for item in test if item['model'] == 'ex10.movies']
        for row in planets:
            for col in colonnes_planets:
                if row['fields'][col] == 'NULL':
                    row['fields'][col] = None
            Planets.objects.get_or_create(
            name=row['fields']['name'],
            defaults={
                'climate': row['fields']['climate'],
                'diameter': row['fields']['diameter'],
                'orbital_period': row['fields']['orbital_period'],
                'population': row['fields']['population'],
                'rotation_period': row['fields']['rotation_period'],
                'surface_water': row['fields']['surface_water'],
                'terrain': row['fields']['terrain'] 
            }
        )
        for row in people:
            for col in colonnes_people:
                if row['fields'][col] == 'NULL':
                    row['fields'][col] = None
            try:
                homeworld_pk = row['fields']['homeworld']
                planet = None
                for item in planets:
                    if item['pk'] == homeworld_pk:
                        planet = Planets.objects.get(name=item['fields']['name'])
                        break
            except:
                planet = None
            People.objects.get_or_create(
                name=row['fields']['name'],
                defaults={
                    'birth_year': row['fields']['birth_year'],
                    'gender': row['fields']['gender'],
                    'eye_color': row['fields']['eye_color'],
                    'hair_color': row['fields']['hair_color'],
                    'height': row['fields']['height'],
                    'mass': row['fields']['mass'],
                    'homeworld': planet 
                }
            )

            for row in movies:
                try:
                    characters_pk = row['fields']['characters']
                    characters = []
                    for item in people:
                        if item['pk'] in characters_pk:
                            characters.append(People.objects.get(name=item['fields']['name']))
                except People.DoesNotExist:
                    pass
                movie, _ = Movies.objects.get_or_create(
                    title=row['fields']['title'],
                    defaults={
                        'episode_nb': row['pk'],
                        'opening_crawl': row['fields']['opening_crawl'],
                        'director': row['fields']['director'],
                        'producer': row['fields']['producer'],
                        'release_date': row['fields']['release_date'],
                    }
                )
                movie.characters.set(characters)
        characters = People.objects.all()
        genre = list({character.gender for character in characters if character})
        if request.method == 'POST':
            diameter = request.POST.get("planet_diameter")
            min_date = request.POST.get("min_date")
            max_date = request.POST.get("max_date")
            sex = request.POST.get("sex")
            find = People.objects.filter(gender=sex, homeworld__diameter__gte=diameter, people__release_date__gt=min_date, people__release_date__lt=max_date).distinct()
            results = []
            for character in find:
                movies = character.people.filter(release_date__gt=min_date, release_date__lt=max_date)
                for movie in movies:
                    results.append({
                        'name': character.name,
                        'gender': character.gender,
                        'title': movie.title,
                        'homeworld': character.homeworld,
                        'diameter': character.homeworld.diameter,
                    })

    return render(request, 'ex10/index.html', {"genre": genre, "results": results})
   
