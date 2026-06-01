import pandas as pd 

df = pd.read_csv("netflix_clean.csv")

print(df.shape)

# highly_rated = df[df['rating'] >= 8.0]
# print(highly_rated.shape)
# print(highly_rated[['title', 'rating']].head(10))

# movies_after_2015 = df[df['year'] > 2015]
# print(movies_after_2015.shape)
# print(movies_after_2015[['title', 'year']]
#       )

# # Filtering for drama movies with rating >7

# drama_movies_with_7_plus_ratings = df[df['genre'].str.contains('drama', case=False) & (df['rating'] > 7)]
# print(drama_movies_with_7_plus_ratings.shape)
# print(drama_movies_with_7_plus_ratings[['title', 'genre', 'rating']].head(5))

# ## get top 5 heighest rated drama movies with rating >7 
 
# top_5_drama_movies = drama_movies_with_7_plus_ratings.sort_values(by='rating', ascending=False).head(5)
# print(top_5_drama_movies[['title', 'genre', 'rating']])

# most_certificated_movies = df[df['certificate'] != 'Not Rated'].sort_values(by='certificate', ascending=False).head(5)
# print(most_certificated_movies[['title', 'certificate']])
 
# top_5_certificated_movies_with_count = df[df['certificate'] != 'Not Rated'].groupby('title').size().sort_values(ascending=False).head(5)
# print(top_5_certificated_movies_with_count)

# total_unique_year = df['year'].nunique()
# print(f"Total unique years: {total_unique_year}")

# print(df['certificate'].value_counts().head(5))

crime_movies = df[df['genre'].str.contains('crime', case=False)]
print(crime_movies.shape)