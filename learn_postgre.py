import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user='postgres', password="1234", port="5432")
cur = conn.cursor()

# Do sth
cur.execute("""
CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INTEGER,
    gender CHAR
);
""")
# Insert Data
cur.execute("""
INSERT INTO person (id, name, age, gender) VALUES
(1, 'MIKE', 30, 'm'),
(2, 'LISA', 30, 'f'),
(3, 'John', 54, 'm'),
(4, 'Bob', 80, 'm'),
(5, 'Julie', 40, 'f')
""")

# Query with 1 fetched results
cur.execute("""SELECT * FROM person WHERE name = 'Bob';""")
print(cur.fetchone())

# Query with more than 1 fetched results, returned as a list
cur.execute("""SELECT * FROM person WHERE age < 50;""")
print(cur.fetchall())

# save the query before execution
sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s""", ("J", 50))
print(sql)
cur.execute(sql)
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()