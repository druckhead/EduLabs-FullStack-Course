import psycopg2
from config import get_config


def using_fetch_one(cur):
    # The  fetchone() fetches the next row in the result set.
    # It returns a single tuple or None when no more row is available.
    result = ""
    while result is not None:
        result = cur.fetchone()
        print(result)


def using_fetch_many(cur):
    # The  fetchmany(size=cursor.arraysize) fetches the next set of rows specified by the
    # size parameter.
    # The  fetchmany() method returns a list of tuples or an empty list if no more rows available.
    print(cur.arraysize)
    result = cur.fetchmany()
    print(result)


def using_fetch_all(cur):
    pass


def demo_query():
    # read connection parameters
    params = get_config()

    # connect to the PostgreSQL server
    print("Connecting to the PostgreSQL database...")
    conn = psycopg2.connect(**params)

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    cur.execute("SELECT * FROM customers")
    # using_fetch_one(cur)
    # using_fetch_many(cur)
    # using_fetch_all(cur)

    conn.close()


if __name__ == "__main__":
    demo_query()
