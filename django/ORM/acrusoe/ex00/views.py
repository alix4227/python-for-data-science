from django.shortcuts import render
import psycopg2


def index(request):
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
            CREATE TABLE IF NOT EXISTS ex00_movies (
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
    return render(request, 'ex00/index.html', {"result": result})
