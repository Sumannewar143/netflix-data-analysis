import pandas as pd 
import sqlite3

df = pd.read_csv('netflix_clean.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('netflix', conn, index=False, if_exists='replace')



result = pd.read_sql("""
WITH avg_rating AS (
    SELECT AVG(rating) AS avg_rating
    FROM netflix
)
SELECT title, genre, rating
FROM netflix, avg_rating
WHERE rating > avg_rating.avg_rating
ORDER BY rating DESC
LIMIT 10;
                     """, conn)


print(result)
# Common Table Expressions (CTEs) 
result_2 = pd.read_sql("""
                       
SELECT title, genre, rating,
                       
AVG(rating) OVER(PARTITION BY genre) AS avg_genre_rating
FROM netflix;
                                      reference
 """, conn)
print(result_2)


result_3 = pd.read_sql("""
SELECT title, genre, rating,
ROW_NUMBER() 
OVER(PARTITION BY genre ORDER BY rating DESC) 
AS rank_in_genre
FROM netflix
LIMIT 5;                       
""", conn)
print(result_3)


result_4 = pd.read_sql("""
SELECT title, genre, rating,
            RANK() OVER (PARTITION BY genre 
            ORDER BY rating DESC  )
            AS rank_in_genre
FROM netflix
LIMIT 7;
                       
""", conn)

print(result_4)                                              

result = pd.read_sql("""
    SELECT 
        year,
        COUNT(*) AS total_releases,
        LAG(COUNT(*)) OVER (ORDER BY year) AS prev_year_releases
    FROM netflix
    GROUP BY year
    ORDER BY year 
                    
""", conn)
print(result)

result = pd.read_sql("""
    SELECT 
        year,
        COUNT(*) AS yearly_releases,
        SUM(COUNT(*)) OVER (ORDER BY year) AS cumulative_releases
    FROM netflix
    GROUP BY year
    ORDER BY year 
                 
                     
""", conn)
print(result)