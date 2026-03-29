import matplotlib.pyplot as plt
from scipy.stats import ttest_ind


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

def statistical_analysis(df):
    expense = df[df['type'] == 'expense']['amount']

    print("\n=== STATISTICAL ANALYSIS ===")
    print(f"Mean: {expense.mean()}")
    print(f"Median: {expense.median()}")
    print(f"Standard Deviation: {expense.std()}")
    print(f"Variance: {expense.var()}")


def correlation_analysis(df):
    df_copy = df.copy()

    # Convert type to numeric
    df_copy['type'] = df_copy['type'].map({'income': 1, 'expense': 0})

    # Select ONLY numeric columns
    numeric_df = df_copy.select_dtypes(include=['number'])

    print("\n=== CORRELATION MATRIX ===")
    print(numeric_df.corr())

def hypothesis_testing(df):
    income = df[df['type'] == 'income']['amount']
    expense = df[df['type'] == 'expense']['amount']

    stat, p_value = ttest_ind(income, expense)

    print("\n=== HYPOTHESIS TESTING ===")
    print(f"P-value: {p_value}")

    if p_value < 0.05:
        print("Reject H0 → Significant difference exists")
    else:
        print("Fail to reject H0 → No significant difference")