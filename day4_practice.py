import pandas as pd 
df = pd.read_csv("netflix_clean.csv")

## Finding yearly performance report for each year 

yearly_report = df.groupby('year').agg(
    total_movies_released= ('title', 'count'),
    average_rating= ('rating', 'mean'),
    total_votes= ('votes', 'sum')

).reset_index()

yearly_report = yearly_report[yearly_report['total_movies_released'] >= 100]

print(yearly_report.sort_values('total_movies_released', ascending=False).head(10))

best_year = yearly_report.loc[yearly_report['average_rating'].idxmax()]
print(best_year)

average_rating_per_genre = df.groupby('genre')['rating'].mean()      
average_rating_per_genre=average_rating_per_genre.sort_values(ascending=False)  
print(average_rating_per_genre.head(5))