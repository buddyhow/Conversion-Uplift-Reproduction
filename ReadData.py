import pandas as pd
sample_size = 500000
chunksize = 100000

samples=[]

for chunk in pd.read_csv("criteo-uplift-v2.1.csv", chunksize=chunksize):
    frac = min(1, sample_size / 13000000)
    samples.append(chunk.sample(frac=frac, random_state=42))

df = pd.concat(samples, ignore_index=True)

df.to_parquet("criteo-uplift-samples.parquet", index=False)