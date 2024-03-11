import psycopg2
from datetime import datetime, timezone
from typing import List

from model import FlatModel


config = {
    "user": "admin",
    "password": "postgres",
    "host": "db",
    "port": "5432",
    "database": "luxonis_db",
}


def insert_flats(flats: List[FlatModel]) -> int:
    utc = datetime.now(timezone.utc)
    tuples = [(f.title, utc, f.img_url) for f in flats]

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            sql = "INSERT INTO flats(title, created, img_url) VALUES(%s, %s, %s)"
            cur.executemany(sql, tuples)
            conn.commit()


def get_all_flats() -> List[FlatModel]:
    flats = []

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            sql = "SELECT title, img_url FROM flats"
            cur.execute(sql)
            records = cur.fetchall()

            for r in records:
                flats.append(FlatModel(r[0], r[1]))

    return flats
