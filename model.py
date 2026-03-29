from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


# ================= LINEAR REGRESSION =================
def predict_expense(df):
    df_exp = df[df['type'] == 'expense'].copy()

    X = df_exp[['day_index']]
    y = df_exp['amount']

    model = LinearRegression()
    model.fit(X, y)

    next_day = pd.DataFrame({
        'day_index': [df_exp['day_index'].max() + 1]
    })

    prediction = model.predict(next_day)

    print("\n=== LINEAR REGRESSION PREDICTION ===")
    print(f"Predicted next expense: {prediction[0]:.2f}")


# ================= LOGISTIC REGRESSION =================
def classify_expense_risk(df):
    df_exp = df[df['type'] == 'expense'].copy()

    df_exp['high_expense'] = (df_exp['amount'] > 1000).astype(int)

    X = df_exp[['day_index']]
    y = df_exp['high_expense']

    model = LogisticRegression()
    model.fit(X, y)

    next_day = pd.DataFrame({
        'day_index': [df_exp['day_index'].max() + 1]
    })

    prediction = model.predict(next_day)

    print("\n=== LOGISTIC REGRESSION ===")
    print(f"High expense risk (1=Yes, 0=No): {prediction[0]}")


# ================= DECISION TREE =================
def decision_tree_model(df):
    df_exp = df[df['type'] == 'expense'].copy()

    df_exp['high_expense'] = (df_exp['amount'] > 1000).astype(int)

    X = df_exp[['day_index']]
    y = df_exp['high_expense']

    model = DecisionTreeClassifier()
    model.fit(X, y)

    next_day = pd.DataFrame({
        'day_index': [df_exp['day_index'].max() + 1]
    })

    prediction = model.predict(next_day)

    print("\n=== DECISION TREE ===")
    print(f"Prediction (1=High, 0=Low): {prediction[0]}")