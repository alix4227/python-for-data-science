from django.shortcuts import render

from ex09.models import *
import datetime
import json

def display(request):
    result = f'No data available,please use the following command line before use:'
    planets = []
    colonnes_planets = ['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']
    colonnes_people = ['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'heigth', 'mass', 'homeworld']

    with open('ex09/ex09_initial_data.json', 'r') as f:
        test = json.load(f)
        planets = [planet for planet in test if planet['model'] == 'ex09.planets']
        people = [item for item in test if item['model'] == 'ex09.people']
        # print(planets)
        for row in planets:
            # for col in colonnes_planets:
            #     if row[col] == 'NULL':
            #         row[col] = None
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
            try:
                planet = Planets.objects.get(name=row['fields']['homeworld'])
            except:
                planet = None
            People.objects.get_or_create(
                name=row['fields']['name'],
                defaults={
                    'birth_year': row['fields']['birth_year'],
                    'gender': row['fields']['gender'],
                    'eye_color': row['fields']['eye_color'],
                    'hair_color': row['fields']['hair_color'],
                    'heigth': row['fields']['heigth'],
                    'mass': row['fields']['mass'],
                    'homeworld': planet 
                }
            )
    # with open('ex09/people.csv', newline='') as f:
    #     reader = csv.DictReader(f, fieldnames=colonnes_people, delimiter='\t')
    #     for row in reader:
    #         for col in colonnes_people:
    #             if row[col] == 'NULL':
    #                 row[col] = None
    #         if row['homeworld'] is None:
    #             continue
    #         planet = Planets.objects.get(name=row['homeworld'])
    #         
    people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name')
    headers = ['name','homeworld','climate']
    return render(request, 'ex09/display.html', {"people": people, "result": result, "headers": headers})

   