
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('african-transaction-dataset.csv')

# Prepare data
X = df[['amount']]  # Using only amount for simplicity
y = df['is_fraud']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction function
def predict_fraud(amount):
    """Predict fraud probability for a transaction amount"""
    probability = model.predict_proba([[amount]])[0][1]
    return probability

# Example usage
if __name__ == "__main__":
    test_amounts = [80000, 5000, 150000, 3000]
    for amount in test_amounts:
        risk = predict_fraud(amount)
        print(f"₦{amount}: Fraud risk = {risk:.0%}")
        if risk > 0.7:
            print("🚨 High risk! Review required")
        else:
            print("✅ Low risk")
