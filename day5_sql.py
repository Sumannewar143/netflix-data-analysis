import pandas as pd 
import sqlite3

df = pd.read_csv('netflix_clean.csv', encoding='latin-1', on_bad_lines='skip')

conn = sqlite3.connect(':memory:')
df.to_sql("netflix_data", conn, index=False, if_exists='replace')

query = """ 
SELECT genre, AVG(rating) as avg_rating, COUNT(*) as total_movies
FROM netflix_data
GROUP BY genre
ORDER BY avg_rating DESC
LIMIT 10;

"""

query2 ="""
SELECT genre, AVG(rating) as avg_rating, COUNT(*) as total_movies
FROM netflix_data
GROUP BY genre
HAVING total_movies >= 50
ORDER BY avg_rating DESC;
"""

result = pd.read_sql_query(query, conn)
print(result)


## Example OF HAVING 

# -- WHERE: filter rows BEFORE grouping
# SELECT genre, COUNT(*) as total
# FROM netflix
# WHERE rating > 7        -- filter individual rows first
# GROUP BY genre;

# -- HAVING: filter groups AFTER grouping
# SELECT genre, COUNT(*) as total
# FROM netflix
# GROUP BY genre
# HAVING total >= 50;     -- filter groups after counting

###  COUNT, AVG, SUM, MIN, MAX
# These are called aggregate functions. They calculate one number from many rows.

# -- How many total movies?
# SELECT COUNT(*) as total_movies
# FROM netflix_data;

# -- Average rating of all movies
# SELECT AVG(rating) as avg_rating
# FROM netflix_data;

# -- Total votes across all movies
# SELECT SUM(votes) as total_votes
# FROM netflix_data;

# -- Highest and lowest rating
# SELECT MAX(rating) as highest, MIN(rating) as lowest
# FROM netflix_data;