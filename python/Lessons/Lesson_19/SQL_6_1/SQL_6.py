from pprint import pprint

import psycopg2
from config import get_config


class IMDB:
    def __init__(self) -> None:
        pass

    @staticmethod
    def contains(movie_name: str):
        data = None

        # read connection parameters
        params = get_config()

        # connect to the PostgreSQL server
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        try:
            with conn:
                with conn.cursor() as curs:
                    query = """
                    SELECT *
                    FROM movies m
                    WHERE m.name ILIKE %s
                    """
                    curs.execute(query, (movie_name,))
                    data = curs.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

        return data

    @staticmethod
    def filter_by_rating(rating: float):
        data = []

        conn = None

        # read connection parameters
        params = get_config()

        # connect to the PostgreSQL server
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        try:
            with conn:
                with conn.cursor() as curs:
                    query = """SELECT *
                        FROM movies
                        WHERE rating > %s;
                        """
                    curs.execute(query, (rating,))
                    row = curs.fetchone()
                    while row is not None:
                        data.append(row)
                        row = curs.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

        return data
