import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", password="1234", port="5432")
cur = conn.cursor()

# Do sth

conn.commit()
cur.close()
conn.close()