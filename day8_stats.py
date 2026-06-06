import pandas as pd

df = pd.read_csv('netflix_clean.csv')

# Mean rating — pulled up by high-rated shows
mean_rating = df['rating'].mean()
print(f"Mean rating: {mean_rating:.2f}")

# Median rating — the true middle, not skewed by outliers
median_rating = df['rating'].median()
print(f"Median rating: {median_rating:.2f}")

# Mode rating — what rating appears most often
mode_rating = df['rating'].mode()[0]
print(f"Mode rating: {mode_rating}")

# Business insight: compare mean vs median
difference = mean_rating - median_rating
if abs(difference) > 0.1:
    print(f"\n⚠ Mean and median differ by {difference:.2f}") 
    print("This suggests the rating data is skewed.")
    print("Report MEDIAN to your manager, not mean.")
else:
    print("\nMean and median are close — data is roughly symmetric.")
    print("Either is acceptable to report.") 



# mean duration 
mean_duration = df['duration'].mean()
print(f"mean duration:{mean_duration:.2f}")

# median duration 
median_duration = df['duration'].median()
print(f"median duration:{median_duration:.2f}")

#mode duration 
mode_duration =df['duration'].mode()[0]
print(f"mode duration:{mode_duration}")

## standard deviation of ratings and votes 

sd_rating = df['rating'].std()
print(sd_rating)
sd_votes = df['votes'].std()
print(sd_votes)