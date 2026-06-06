import pandas as pd 

df = pd.read_csv("netflix_clean.csv")

print(df.shape)

# average rating by genre 
genre_rating = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
print(genre_rating)

# Count of movies per genre
genre_count = df.groupby('genre')['title'].count()
print(genre_count.sort_values(ascending=False).head(10))

# Total votes per genre
genre_votes = df.groupby('genre')['votes'].sum()
print(genre_votes.sort_values(ascending=False).head(10))

# Highest rated movie per genre
genre_max = df.groupby('genre')['rating'].max()
print(genre_max.sort_values(ascending=False).head(10))
 

# Multiple aggregations on rating by genre

genre_analysis = df.groupby('genre').agg(
    average_rating=('rating', 'mean'),
    total_movies=('title', 'count'),
    total_votes=('votes','sum'),
    highest_rating=('rating','max'),
    lowest_rating=('rating', 'min')

).sort_values('average_rating', ascending=False)

print(genre_analysis.head(10))

# Without reset_index — genre is the index
result = df.groupby('genre')['rating'].mean()
print(type(result))  # Series, not DataFrame

# With reset_index — genre becomes a regular column again
result = df.groupby('genre')['rating'].mean().reset_index()
print(result.head())  # Proper DataFrame with 2 columns

# Average rating by genre AND certificate
multi_group = df.groupby(['genre', 'certificate'])['rating'].mean()
print(multi_group.head(15))

# Count movies by year AND genre
year_genre = df.groupby(['year', 'genre'])['title'].count().reset_index()
year_genre.columns = ['year', 'genre', 'movie_count']
print(year_genre.sort_values('movie_count',ascending=False).head(10))


#### complete genre performance report showing 

genre_report = df.groupby('genre').agg(
    average_rating=('rating', 'mean'),
    total_movies=('title', 'count'),
    total_votes=('votes', 'sum')
).reset_index()

# Filter genres with at least 50 movies
genre_report_filtered = genre_report[genre_report['total_movies'] >= 50]

# Now sort by average rating
genre_report_filtered = genre_report_filtered.sort_values(
    'average_rating', ascending=False)

print(genre_report_filtered.head(10))

total_genres = genre_report['genre'].nunique()
genres_kept = genre_report_filtered['genre'].nunique()
print(f"Total genres: {total_genres}")
print(f"Genres with 50+ movies: {genres_kept}")
print(f"Genres filtered out: {total_genres - genres_kept}")