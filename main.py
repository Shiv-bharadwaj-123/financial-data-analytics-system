from utils import load_data, clean_data, preprocess_data, save_to_sql

df = load_data()
df = clean_data(df)
df = preprocess_data(df)
save_to_sql(df)

# print(df)
# print("Data saved to SQL database successfully")
# print("\nData Types:")
# print(df.dtypes)

import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM transactions")
rows = cursor.fetchall()

print("\nData from SQL:")
for row in rows:
    print(row)

conn.close()