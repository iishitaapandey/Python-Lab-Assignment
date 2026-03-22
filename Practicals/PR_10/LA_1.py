import pandas as pd

df = pd.read_csv("books.csv")

df.columns = df.columns.str.strip()

df["author"] = df["author"].str.strip().str.lower()
df["publisher"] = df["publisher"].str.strip().str.lower()

print("\n--- All Books ---")
print(df.to_string(index=False))

author = input("\nEnter author name: ").lower().strip()
result = df[df["author"] == author]

if result.empty:
    print("No books found")
else:
    print(result.to_string(index=False))

pub = input("\nEnter publisher: ").lower().strip()
result = df[df["publisher"] == pub]

if result.empty:
    print("No books found")
else:
    print(result.to_string(index=False))

print("\nCheapest Book:")
print(df.loc[df["price"].idxmin()][["title", "price"]])

print("\nCostliest Book:")
print(df.loc[df["price"].idxmax()][["title", "price"]])

print("\nSorted by Year:")
print(df.sort_values(by="year").to_string(index=False))