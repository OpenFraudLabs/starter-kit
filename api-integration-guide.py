from openfraudlabs import FraudDetector

# Initialize with Africa-optimized model
detector = FraudDetector(api_key="YOUR_API_KEY", region="africa")

# Example transaction
transaction = {
    "amount": 25000,
    "currency": "NGN",
    "merchant": "POS_12345",
    "user_id": "USER_67890",
    "location": "Lagos, NG"
}

# Get fraud prediction
result = detector.analyze(transaction)

if result['risk_score'] > 0.85:
    print("🚨 High fraud risk! Trigger manual review")
else:
    print("✅ Transaction approved")
