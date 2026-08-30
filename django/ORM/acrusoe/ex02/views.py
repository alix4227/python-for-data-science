from django.shortcuts import render
import psycopg2

def init(request):
    conn = None
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
                CREATE TABLE IF NOT EXISTS ex02_movies (
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
        conn.close()
   
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = e
    return render(request, 'ex00/index.html', {"result": result})

def populate(request):
    conn = None
    try:
        conn = psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5433"
    )

        with conn.cursor() as cur:
            movies = [
            ('The Phantom Menace',        1, 'George Lucas',    'Rick McCallum',                                       '1999-05-19'),
            ('Attack of the Clones',      2, 'George Lucas',    'Rick McCallum',                                       '2002-05-16'),
            ('Revenge of the Sith',       3, 'George Lucas',    'Rick McCallum',                                       '2005-05-19'),
            ('A New Hope',                4, 'George Lucas',    'Gary Kurtz, Rick McCallum',                           '1977-05-25'),
            ('The Empire Strikes Back',   5, 'Irvin Kershner',  'Gary Kutz, Rick McCallum',                           '1980-05-17'),
            ('Return of the Jedi',        6, 'Richard Marquand','Howard G. Kazanjian, George Lucas, Rick McCallum',   '1983-05-25'),
            ('The Force Awakens',         7, 'J. J. Abrams',    'Kathleen Kennedy, J. J. Abrams, Bryan Burk',         '2015-12-11'),
            ]
            cur.executemany("""
                INSERT INTO ex02_movies (title, episode_nb, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s);
            """, movies)
        conn.commit()
        result = 'OK'
        conn.close()
   
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = e
    return render(request, 'ex00/index.html', {"result": result})

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

        with conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM ex02_movies;
            """)
            table = cur.fetchall()
            conn.close()
            result = "No data available"
        
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = "No data available"
    return render(request, 'ex02/index.html', {"result": result, "titles": titles, "table": table})