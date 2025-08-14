import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('african-transaction-dataset.csv')

# Prepare data
X = df[['amount']]  # Simple feature
y = df['is_fraud']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction function
def predict_fraud(amount):
    return model.predict([[amount]])[0]

# Test
print(predict_fraud(80000))  # Likely fraud (1)
print(predict_fraud(5000))   # Likely legit (0)
