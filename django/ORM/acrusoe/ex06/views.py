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
            CREATE TABLE IF NOT EXISTS ex06_movies (
                title           VARCHAR(100) NOT NULL UNIQUE,
                episode_nb      INTEGER PRIMARY KEY,
                opening_crawl   TEXT,
                director        VARCHAR(32) NOT NULL,
                producer        VARCHAR(128) NOT NULL,
                release_date    DATE NOT NULL,
                created         TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                updated         TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            )
        """)

        cur.execute("""
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
            END;
            $$ language 'plpgsql'
        """)

        cur.execute("""
            CREATE OR REPLACE TRIGGER update_films_changetimestamp
            BEFORE UPDATE ON ex06_movies
            FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column()
        """)

        conn.commit()
        conn.commit()
        result = 'OK'
        cur.close()
        conn.close()
   
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = e
    return render(request, 'ex06/index.html', {"result": result})


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
                INSERT INTO ex06_movies (title, episode_nb, director, producer, release_date)
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
    return render(request, 'ex06/index.html', {"result": result})

def display(request):
    conn = None
    titles = ['title','episode_nb','opening_crawl', 'director', 'producer', 'release_date', 'created', 'updated']
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
            FROM ex06_movies;
        """)
        table = cur.fetchall()
        cur.close()
        conn.close()
        result = "No data available"
        
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        result = "No data available"
    return render(request, 'ex06/display.html', {"result": result, "titles": titles, "table": table})


def update(request):
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
            input = request.POST.get('input')
            cur.execute("""
                UPDATE ex06_movies
                SET opening_crawl = %s
                WHERE title = %s;
            """, [input, movie_selected])
            conn.commit()
        cur.execute("""
            SELECT title
            FROM ex06_movies;
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
    return render(request, 'ex06/update.html', {"result": result, "titles": titles})