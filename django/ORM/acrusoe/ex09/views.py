from django.shortcuts import render

from ex09.models import *
import json

def display(request):
    result = f'No data available, please use the following command line before use:\n "python manage.py makemigrations ex09"\n "python manage.py migrate ex09"\n'
    planets = []
    people = []
    colonnes_planets = ['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']
    colonnes_people = ['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld']

    with open('ex09/ex09_initial_data.json', 'r') as f:
        test = json.load(f)
        planets = [planet for planet in test if planet['model'] == 'ex09.planets']
        people = [item for item in test if item['model'] == 'ex09.people']

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
    p = People.objects.filter(homeworld__climate__icontains='windy').order_by('name')
    headers = ['name','homeworld','climate']
    return render(request, 'ex09/display.html', {"people": p, "result": result, "headers": headers})

   