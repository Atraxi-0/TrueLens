# scripts/merge_clean.py
import pandas as pd

df_real = pd.read_csv('dataset/real_news.csv')
df_fake = pd.read_csv('dataset/fake_news.csv')

# Combine
df = pd.concat([df_real, df_fake], ignore_index=True)

# Clean text (optional: remove special characters, lowercasing, etc.)
df.dropna(inplace=True)
df['text'] = df['text'].str.replace(r'\s+', ' ', regex=True)

# Save
df.to_csv('dataset/indian_fake_news_dataset.csv', index=False)
