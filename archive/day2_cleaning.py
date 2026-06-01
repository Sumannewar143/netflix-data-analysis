import pandas as pd
df = pd.read_csv("data.csv", encoding='latin-1')

# Step 1 - See missing values
print(df.isnull().sum())
print(f"Original shape: {df.shape}")

# Step 2 - Drop rows where rating is missing + add .copy()
df_clean = df.dropna(subset=['rating']).copy()
print(f"After dropping missing ratings: {df_clean.shape}")

# Step 3 - Fill missing certificate
df_clean['certificate'] = df_clean['certificate'].fillna('Not Rated')

# Step 4 - Fix duration: remove " min", convert to number, fill median
df_clean['duration'] = df_clean['duration'].str.replace(' min', '').str.strip()
df_clean['duration'] = pd.to_numeric(df_clean['duration'], errors='coerce')
df_clean['duration'] = df_clean['duration'].fillna(df_clean['duration'].median())

# Step 5 - Fill missing genre
df_clean['genre'] = df_clean['genre'].fillna('Unknown')

# Step 6 - Fill missing year with median
# Extract 4 digit year from text like "(2020)" or "2020–2023"
df_clean['year'] = df_clean['year'].astype(str).str.extract(r'(\d{4})')[0]
df_clean['year'] = pd.to_numeric(df_clean['year'], errors='coerce')
df_clean['year'] = df_clean['year'].fillna(df_clean['year'].median())

# Step 7 - Fix votes column same as duration
df_clean['votes'] = pd.to_numeric(
    df_clean['votes'].astype(str).str.replace(',', ''), 
    errors='coerce'
)

# Step 8 - Verify
print(df_clean.isnull().sum())
print(f"Final clean shape: {df_clean.shape}")

# Step 9 - Save
df_clean.to_csv("netflix_clean.csv", index=False)
print("Clean file saved!")