import pandas as pd
import random

# Load your test CSV
df = pd.read_csv(r'D:\Projects\TrueLens\dataset\test_data.csv')

# Ensure binary labels: 0 = real, 1 = fake
df = df[df['label'].isin([0, 1])]

def get_random_sample(label):
    subset = df[df['label'] == label]
    if subset.empty:
        return "No sample found"
    return random.choice(subset['text'].dropna().tolist())
