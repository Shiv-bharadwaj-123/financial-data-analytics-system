import matplotlib.pyplot as plt


def basic_analysis(df):
    income = df[df['type'] == 'income']['amount'].sum()
    expense = df[df['type'] == 'expense']['amount'].sum()

    print("\n=== BASIC ANALYSIS ===")
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Savings: {income - expense}")



def category_analysis(df):
    expense_df = df[df['type'] == 'expense']

    print("\n=== CATEGORY-WISE EXPENSE ===")
    print(expense_df.groupby('category')['amount'].sum())



def plot_expense(df):
    expense_df = df[df['type'] == 'expense']

    expense_df.groupby('category')['amount'].sum().plot(kind='bar')

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()