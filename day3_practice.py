import pandas as pd

# Load dataset
df = pd.read_csv("netflix_clean.csv")

## 1. 10 highest rated movies of all time in our dataset

top_10_movies = df.sort_values(by='rating', ascending=False).head(10)
print(top_10_movies[['title', 'year', 'rating']])

## 2. How many Action movies have rating above 7?

action_movies_above_7 = df[df['genre'].str.contains('Action', case=False) & (df['rating'] > 7)]
print(action_movies_above_7.shape[0])

## 3. Which 3 years had the most content added?

top_3_years = df['year'].value_counts().head(3)
print(top_3_years)

## 4. What percentage of our content is TV-MA?"

percentage_tv_ma = (df['certificate'] == 'TV-MA').mean() * 100
print(f"percentage_tv_ma: {percentage_tv_ma:.2f}%")

