from utils import load_data, clean_data, preprocess_data, save_to_sql
from analysis import basic_analysis, category_analysis
from analysis import plot_expense

df = load_data()
df = clean_data(df)
df = preprocess_data(df)
save_to_sql(df)
basic_analysis(df)
category_analysis(df)

plot_expense(df)

# print(df)
# print("Data saved to SQL database successfully")
# print("\nData Types:")
# print(df.dtypes)

# import sqlite3
#
# conn = sqlite3.connect("finance.db")
# cursor = conn.cursor()
#
# cursor.execute("SELECT * FROM transactions")
# rows = cursor.fetchall()
#
# print("\nData from SQL:")
# for row in rows:
#     print(row)
#
# conn.close()