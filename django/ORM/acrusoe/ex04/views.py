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

        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                title           VARCHAR(100) NOT NULL UNIQUE,
                episode_nb      INTEGER PRIMARY KEY,
                opening_crawl   TEXT,
                director        VARCHAR(32) NOT NULL,
                producer        VARCHAR(128) NOT NULL,
                release_date    DATE NOT NULL
            )
        """)
        conn.commit()
        result = 'OK'
        cur.close()
        conn.close()
   
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = e
    return render(request, 'ex04/index.html', {"result": result})


def populate(request):
    conn = None
    result = []
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )

        cur = conn.cursor()
        movies = [
        ('The Phantom Menace',        1, 'George Lucas',    'Rick McCallum',                                       '1999-05-19'),
        ('Attack of the Clones',      2, 'George Lucas',    'Rick McCallum',                                       '2002-05-16'),
        ('Revenge of the Sith',       3, 'George Lucas',    'Rick McCallum',                                       '2005-05-19'),
        ('A New Hope',                4, 'George Lucas',    'Gary Kurtz, Rick McCallum',                           '1977-05-25'),
        ('The Empire Strikes Back',   5, 'Irvin Kershner',  'Gary Kutz, Rick McCallum',                           '1980-05-17'),
        ('Return of the Jedi',        6, 'Richard Marquand','Howard G. Kazanjian, George Lucas, Rick McCallum',   '1983-05-25'),
        ('The Force Awakens',         7, 'J. J. Abrams',    'Kathleen Kennedy, J. J. Abrams, Bryan Burk',         '2015-12-11'),
        ]

        for movie in movies:
            cur.execute("""
                INSERT INTO ex04_movies (title, episode_nb, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (title) DO NOTHING;        
            """,  movie)
            result.append('OK')
            conn.commit()
        cur.close()
        conn.close()
   
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result.append(e)
    return render(request, 'ex04/index.html', {"result": result})

def display(request):
    conn = None
    titles = ['title','episode_nb','opening_crawl', 'director', 'producer', 'release_date']
    table = []
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )

        cur = conn.cursor()
        cur.execute("""
            SELECT *
            FROM ex04_movies;
        """)
        table = cur.fetchall()
        cur.close()
        conn.close()
        if request.method == 'POST':
            print('ALIX')
        result = "No data available"
        
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = "No data available"
    return render(request, 'ex04/display.html', {"result": result, "titles": titles, "table": table})


def remove(request):
    conn = None
    titles = ['title','episode_nb','opening_crawl', 'director', 'producer', 'release_date']
    table = []
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )
        cur = conn.cursor()
        if request.method == "POST":
            movie_selected = request.POST.get('movies')
            cur.execute("""
                DELETE FROM ex04_movies
                WHERE title = %s;
            """, [movie_selected])
        cur.execute("""
            SELECT title
            FROM ex04_movies;
        """)
        titles = [row[0] for row in cur.fetchall()]
        conn.commit()
        cur.close()
        conn.close()
        result = "No data available"
        
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = "No data available"
    return render(request, 'ex04/remove.html', {"result": result, "titles": titles})