import pandas as pd

df = pd.read_parquet("criteo-uplift-samples.parquet")

print(df.head())

# Here I'm checking Treatment Populations similarity using distributions and summary statistics

    # Checking Control vs Treatment Population Sizes (full dataset has 85% treatment - sample should mimic this) 
print(df["treatment"].value_counts(normalize=True))

    # Comparing feature means as quick sanitary check
print(df.groupby("treatment").mean(numeric_only=True))

    # All looking good, now plotting some feature distributions using KDE plots

import matplotlib.pyplot as plt
import seaborn as sns

features = ["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11"]

for f in features:
    sns.kdeplot(df[df["treatment"] == 0][f], label="Control")
    sns.kdeplot(df[df["treatment"] == 1][f], label="Treatment")

    plt.legend()
    plt.title(f"Distribution check: {f}")
    plt.show()