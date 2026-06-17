from django.shortcuts import render

from ex09.models import *
import datetime
import csv

def display(request):
    result = f'No data available,please use the following command line before use:'
    planets = []
    colonnes_planets = ['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']
    colonnes_people = ['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'heigth', 'mass', 'homeworld']

    with open('ex09/planets.csv', newline='') as f:
        reader = csv.DictReader(f, fieldnames=colonnes_planets, delimiter='\t')
        for row in reader:
            for col in colonnes_planets:
                if row[col] == 'NULL':
                    row[col] = None
            Planets.objects.get_or_create(
            name=row['name'],
            defaults={
                'climate': row['climate'],
                'diameter': row['diameter'],
                'orbital_period': row['orbital_period'],
                'population': row['population'],
                'rotation_period': row['rotation_period'],
                'surface_water': row['surface_water'],
                'terrain': row['terrain'] 
            }
        )
    with open('ex09/people.csv', newline='') as f:
        reader = csv.DictReader(f, fieldnames=colonnes_people, delimiter='\t')
        for row in reader:
            for col in colonnes_people:
                if row[col] == 'NULL':
                    row[col] = None
            if row['homeworld'] is None:
                continue
            planet = Planets.objects.get(name=row['homeworld'])
            People.objects.get_or_create(
            name=row['name'],
            defaults={
                'birth_year': row['birth_year'],
                'gender': row['gender'],
                'eye_color': row['eye_color'],
                'hair_color': row['hair_color'],
                'heigth': row['heigth'],
                'mass': row['mass'],
                'homeworld': planet 
            }
        )
    people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name')
    headers = ['name','homeworld','climate']
    return render(request, 'ex09/display.html', {"people": people, "result": result, "headers": headers})

   