import psycopg2

# connection string
conn = psycopg2.connect("dbname=best_bus_ever_company user=postgres")

# as params
# conn = psycopg2.connect(
#     host="localhost",
#     port=5432,
#     database="bank",
#     user="postgres",
#     password="postgres")

print(conn)

cur = conn.cursor()

cur.execute(
    """
    SELECT *
    FROM drivers;
    """
)

row = cur.fetchone()
print(row)

cur.close()
conn.close()

print(conn)
