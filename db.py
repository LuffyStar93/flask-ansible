import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="luffystar93",
    )

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mytable (id INT);")
# cur.execute("INSERT INTO mytable (ID) VALUES (1) ")
conn.commit()


