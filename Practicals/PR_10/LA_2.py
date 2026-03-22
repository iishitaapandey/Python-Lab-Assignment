import pandas as pd

data = {
    "State": ["A", "B", "C", "D", "E"],
    "Area": [100, 200, 150, 300, 250],
    "Population": [1000, 5000, 3000, 7000, 6000]
}

df = pd.DataFrame(data)

# a) full info
print("\nAll States:\n", df)

# b) largest area
print("\nLargest Area State:")
print(df.loc[df["Area"].idxmax()]["State"])

# c) largest population
print("\nLargest Population State:")
print(df.loc[df["Population"].idxmax()]["State"])

# d) population density
df["Density"] = df["Population"] / df["Area"]
print("\nWith Density:\n", df)

# e) highest density
print("\nHighest Density State:")
print(df.loc[df["Density"].idxmax()]["State"])