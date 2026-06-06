import pandas as pd 

df = pd.read_csv("data.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())


# # Q1 - How many unique genres are there?
print(df['genre'].nunique())

# # Q2 - What is the highest rated movie?
print(df[df['rating'] == df['rating'].max()])

# #Q3 - What year had most movies? — try this yourself first
print(df['year'].value_counts().idxmax())

# # First convert votes from text to number
df['votes'] = pd.to_numeric(df['votes'].str.replace(',', ''), errors='coerce')

# # Q4 - What is the movie with the most votes?
print(df.sort_values('votes', ascending=False).head(1)[['title', 'votes']])

# # Q5 - How many movies have rating above 8? — try yourself
print(df[df['rating'] > 8].shape[0])
