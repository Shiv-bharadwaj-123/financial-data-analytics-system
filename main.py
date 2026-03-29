from utils import load_data, clean_data

df = load_data()
df = clean_data(df)

print(df)

print("\nData Types:")
print(df.dtypes)