import pandas as pd
import sqlite3

df = pd.read_csv('netflix_clean.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('netflix', conn, index=False, if_exists='replace')

# Check it loaded correctly
# result = pd.read_sql("SELECT COUNT(*) AS total_rows FROM netflix", conn)
# print(result)

result = pd.read_sql("""
    SELECT genre, COUNT(*) AS total_titles
    FROM netflix
    GROUP BY genre
    ORDER BY total_titles DESC
    LIMIT 10
""", conn)
print(result)

result = pd.read_sql("""
    SELECT genre, 
           ROUND(AVG(rating), 2) AS avg_rating,
           COUNT(*) AS total_titles
    FROM netflix
    GROUP BY genre
    HAVING COUNT(*) > 50
    ORDER BY avg_rating DESC
    LIMIT 10
""", conn)
print(result)

result = pd.read_sql("""
    SELECT year, COUNT(*) AS total_releases
    FROM netflix
    GROUP BY year
    ORDER BY total_releases DESC
    LIMIT 10
""", conn)
print(result)


result = pd.read_sql("""
    SELECT title, genre, year, rating 
    FROM netflix
    WHERE rating  > (SELECT AVG(rating) FROM netflix)
    ORDER BY rating DESC
    LIMIT 15;
 """, conn)
print(result)

result = pd.read_sql("""
    SELECT title, year, rating, votes
    FROM netflix
    WHERE title = 'Avatar: The Last Airbender'
""", conn)
print(result)


result = pd.read_sql("""
                     
    SELECT n.title, n.genre, n.year, n.rating, n.votes
FROM netflix n
INNER JOIN (
    SELECT title, MAX(votes) AS max_votes
    FROM netflix
    GROUP BY title
    HAVING MAX(votes) > 1000                      
) AS best
ON n.title = best.title 
AND n.votes = best.max_votes
                  
ORDER BY n.rating DESC
LIMIT 15;                 
                     """, conn)
print(result)