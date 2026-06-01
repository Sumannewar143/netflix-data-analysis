import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_clean.csv", encoding='latin-1', on_bad_lines='skip')

# Top 10 genres by average rating (50+ movies only)
genre_report = df.groupby('genre').agg(
    avg_rating=('rating', 'mean'),
    total_movies=('title', 'count')
).reset_index()

filtered = genre_report[genre_report['total_movies'] >= 50]
top10 = filtered.sort_values('avg_rating', ascending=False).head(10)

plt.figure(figsize=(12, 7))
plt.barh(top10['genre'], top10['avg_rating'], color='steelblue')
plt.xlabel('Average Rating')
plt.title('Top 10 Netflix Genres by Average Rating\n(Genres with 50+ titles only)')
plt.tight_layout()
plt.savefig('netflix_genre_chart.png', dpi=150)
plt.show()
print("Chart saved!")