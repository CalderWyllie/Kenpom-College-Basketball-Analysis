import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading and Cleaning
df = pd.read_csv("KenpomRatings.csv", header=1)

df.columns = (
    df.columns.astype(str)
    .str.replace('\xa0', ' ', regex=False)
    .str.replace(r'\s+', ' ', regex=True)
    .str.strip()
)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print("Columns:", df.columns.tolist())

# Calculating the Win Percentage of Each Team
df[['Wins', 'Losses']] = df['W-L'].str.split('-', expand=True).astype(int)
df['WinPct'] = df['Wins'] / (df['Wins'] + df['Losses'])

num_cols = ['NetRtg','ORtg','DRtg','AdjT','Luck','Strength of Schedule','NCSOS']
for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

print(df.head())


# Question 1: Average Tempo by Conference 

tempo_by_conf = (
    df.groupby("Conf")["AdjT"]
      .mean()
      .sort_values(ascending=False)
)

print("Average Adjusted Tempo (by Conference):")
print(tempo_by_conf)


plt.figure(figsize=(10,6))
sns.barplot(x=tempo_by_conf.values, y=tempo_by_conf.index, palette="coolwarm")
plt.title("Average Tempo by Conference (KenPom Data)")
plt.xlabel("Adjusted Tempo (AdjT)")
plt.ylabel("Conference")
plt.tight_layout()
plt.show()

# Question 2: Strength of Schedule vs. Offensive Efficiency

sos_col = 'NetRtg.1'  
ortg_col = 'ORtg'

df[sos_col]  = pd.to_numeric(df[sos_col], errors='coerce')
df[ortg_col] = pd.to_numeric(df[ortg_col], errors='coerce')


plt.figure(figsize=(8,6))
sns.regplot(x=sos_col, y=ortg_col, data=df, scatter_kws={'alpha':0.6})
plt.title("Strength of Schedule (NetRtg.1) vs Offensive Rating (ORtg)")
plt.xlabel("Strength of Schedule (NetRtg.1)")
plt.ylabel("Offensive Rating (ORtg)")
plt.tight_layout()
plt.show()


corr_val = df[[sos_col, ortg_col]].corr().iloc[0,1]
print(f"Correlation between {sos_col} and {ortg_col}: {corr_val:.3f}")

df['CombinedScore'] = (
    (df[ortg_col] - df[ortg_col].mean()) / df[ortg_col].std() +
    (df[sos_col] - df[sos_col].mean()) / df[sos_col].std()
)

top_combined = df[['Team', 'Conf', ortg_col, sos_col, 'CombinedScore']] \
                  .sort_values('CombinedScore', ascending=False) \
                  .head(10)

print("\nTop 10 Teams Combining High Offensive Efficiency and Strength of Schedule:")
print(top_combined.to_string(index=False))

# Question 3: Underrated Teams

ortg_col = 'ORtg'
drtg_col = 'DRtg'
win_col  = 'WinPct'

for col in [ortg_col, drtg_col, win_col]:
    df[col] = pd.to_numeric(df[col], errors='coerce')


df['z_ORtg'] = (df[ortg_col] - df[ortg_col].mean()) / df[ortg_col].std()
df['z_DRtg'] = (df[drtg_col] - df[drtg_col].mean()) / df[drtg_col].std()
df['z_WinPct'] = (df[win_col] - df[win_col].mean()) / df[win_col].std()


df['UnderratedIndex'] = df['z_ORtg'] - df['z_DRtg'] - df['z_WinPct']


underrated = df[['Team', 'Conf', ortg_col, drtg_col, win_col, 'UnderratedIndex']] \
                .sort_values('UnderratedIndex', ascending=False) \
                .head(10)

print("\n Top 10 'Underrated' Teams (strong both ends, underperformed record):")
print(underrated.to_string(index=False))

plt.figure(figsize=(8,6))
sns.scatterplot(x='WinPct', y='UnderratedIndex', data=df, alpha=0.6)
plt.title("Underrated Index vs Win Percentage")
plt.xlabel("Win Percentage")
plt.ylabel("Underrated Index (High = Underrated)")
plt.tight_layout()
plt.show()

# Scaled version that auto-penalizes high-win teams 
# Magnifies gaps for low-win teams even without a hard cutoff.
df['UnderratedIndex_scaled'] = (df['z_ORtg'] - df['z_DRtg']) * (1 - df[win_col])

underrated_scaled = (
    df[['Team','Conf', ortg_col, drtg_col, win_col, 'UnderratedIndex_scaled']]
    .sort_values('UnderratedIndex_scaled', ascending=False)
    .head(10)
)

print("\n Top 10 by Scaled Underrated Index ( (z_ORtg - z_DRtg) * (1 - WinPct) ):")
print(underrated_scaled.to_string(index=False))