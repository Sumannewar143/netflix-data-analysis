import pandas as pd

df = pd.read_csv("netflix_clean.csv")

print("=" * 40)
print("NETFLIX PLATFORM — STATS SUMMARY")
print("=" * 40)

# ---------------- RATINGS ----------------

print("\nRATINGS")

mean_rating = df["rating"].mean()
median_rating = df["rating"].median()
std_rating = df["rating"].std()

print(f"Mean Rating: {mean_rating:.2f}")
print(f"Median Rating: {median_rating:.2f}")
print(f"Std Dev: {std_rating:.2f}")

distribution = (
    "Right-Skewed" if mean_rating > median_rating
    else "Left-Skewed" if mean_rating < median_rating
    else "Symmetric"
)

top10 = df["rating"].quantile(0.90)

Q1 = df["rating"].quantile(0.25)
Q3 = df["rating"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["rating"] < Q1 - 1.5 * IQR) |
    (df["rating"] > Q3 + 1.5 * IQR)
]

print(f"Distribution:      {distribution}")
print(f"Top 10% threshold: {top10:.2f}+")
print(f"Outliers found:    {len(outliers)} titles")

# ---------------- DURATION ----------------

print("\nDURATION")

print(f"Mean Duration:   {df['duration'].mean():.2f}")
print(f"Median Duration: {df['duration'].median():.2f}")

longest = df.loc[df["duration"].idxmax()]

Q1 = df["duration"].quantile(0.25)
Q3 = df["duration"].quantile(0.75)
IQR = Q3 - Q1

unusually_long = df[
    df["duration"] > (Q3 + 1.5 * IQR)
]

print(f"Longest title:   {longest['title']} ({longest['duration']} min)")
print(f"Unusually long:  {len(unusually_long)} titles")

# ---------------- CORRELATION ----------------

print("\nRELATIONSHIPS")

def strength(r):
    r = abs(r)
    if r < 0.1:
        return "Negligible"
    elif r < 0.4:
        return "Weak"
    elif r < 0.7:
        return "Moderate"
    else:
        return "Strong"

votes_rating = df["votes"].corr(df["rating"])
year_rating = df["year"].corr(df["rating"])

print(
    f"Votes ↔ Rating: r = {votes_rating:.3f} "
    f"({strength(votes_rating)} {'positive' if votes_rating > 0 else 'negative'})"
)

print(
    f"Year ↔ Rating:  r = {year_rating:.3f} "
    f"({strength(year_rating)} {'positive' if year_rating > 0 else 'negative'})"
)

print("RECOMENDATION ")
print("The Netflix catalog shows generally consistent ratings, with most titles clustered around 7/10. Top-performing content begins at a rating of approximately 8.2. A small number of low-rated titles pull the average slightly downward, while a limited set of unusually long titles increase the average duration. Additionally, popularity (votes) has only a weak relationship with ratings, suggesting audience engagement alone is not a strong indicator of perceived quality. Release year also shows almost no relationship with ratings, indicating content quality has remained relatively stable across time")
print("=" *40)