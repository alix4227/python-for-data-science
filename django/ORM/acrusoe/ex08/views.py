from django.shortcuts import render

import psycopg2

def init(request):
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS ex08_planets (
                    id              SERIAL PRIMARY KEY,
                    name            VARCHAR(64) UNIQUE NOT NULL,
                    climate         VARCHAR,
                    diameter        INTEGER,
                    orbital_period  INTEGER,
                    population      BIGINT,
                    rotation_period INTEGER,
                    surface_water   REAL,
                    terrain         VARCHAR(128)
                )
            """)
            conn.commit()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS ex08_people (
                    id              SERIAL PRIMARY KEY,
                    name            VARCHAR(64) UNIQUE NOT NULL,
                    birth_year      VARCHAR(32),
                    gender          VARCHAR(32),
                    eye_color       VARCHAR(32),
                    hair_color      VARCHAR(32),
                    height          INTEGER,
                    mass            REAL,
                    homeworld       VARCHAR(64) REFERENCES ex08_planets(name)
                )
            """)
            conn.commit()
            result = 'OK'
            conn.close()
   
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = e
    return render(request, 'ex08/index.html', {"result": result})


def populate(request):
    conn = None
    results = []
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )
        with conn.cursor() as cur:
            with open('ex08/planets.csv', 'r') as file:
                cur.copy_from(file, 'ex08_planets', columns=(
            'name', 'climate', 'diameter', 'orbital_period',
            'population', 'rotation_period', 'surface_water', 'terrain'
        ), null='NULL')
            results.append('OK')
            with open('ex08/people.csv', 'r') as f:
                cur.copy_from(f, 'ex08_people', columns=(
            'name', 'birth_year', 'gender', 'eye_color',
            'hair_color', 'height', 'mass', 'homeworld'
        ), null='NULL')
            results.append('OK')
            conn.commit()
            conn.close()
        
    except Exception as e:
        if conn:
            conn.rollback()
        results.append(e)
    return render(request, 'ex08/populate.html', {"results": results})

def display(request):
    conn = None
    titles = ['name','planet','climate']
    table = []
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )

        with conn.cursor() as cur:
            cur.execute("""
                SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
                FROM ex08_people
                JOIN ex08_planets ON ex08_people.homeworld = ex08_planets.name
                WHERE ex08_planets.climate LIKE %s
                ORDER BY ex08_people.name ASC
            """, ('%windy%',))
            table = cur.fetchall()
            conn.close()
            result = "No data available"
        
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = "No data available"
    return render(request, 'ex08/display.html', {"result": result, "titles": titles, "table": table})


