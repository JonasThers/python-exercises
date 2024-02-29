import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

cursor = conn.cursor()
cursor.execute("DROP TABLE if exists movie_reviews")

conn.execute('''CREATE TABLE movie_reviews 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             score INTEGER NOT NULL
             )
             ''')

movie_reviews = [
    (
        "A Clockwork Orange",
        9
    ),
    (
        "Dune",
        7
    ),
    (
        "The Iron Giant",
        9
    ),
    (
        "Poor Things",
        8
    )
]

conn.executemany("INSERT INTO movie_reviews(id,name,score) \
                 VALUES ( NULL, ?, ? )", movie_reviews);

print("All movies:")
all_movies = conn.execute("SELECT id, name, score from movie_reviews")
for row in all_movies:
    print (row[0], row[1], row[2])

print("Best movies:")
best_movies = conn.execute("SELECT * from movie_reviews WHERE score >= 9")
for row in best_movies:
    print (row[0], row[1], row[2])

print("Worst movies:")
worst_movies = conn.execute("SELECT * from movie_reviews WHERE score <= 9")
for row in worst_movies:
    print (row[0], row[1], row[2])

print("Let's delete those")
conn.execute("DELETE from movie_reviews WHERE score < 9")

print("Deletion completed")

print("Let's make the good movies perfect!")
conn.execute("UPDATE movie_reviews set score = 10 WHERE score >= 9")

print("Now we only have 10/10 movies")

conn.commit()

conn.close()