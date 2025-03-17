# apps/fraud/utils.py
from sklearn.ensemble import RandomForestClassifier
import numpy as np


# Dummy model (replace with a real one later)
def predict_fraud(features):
    model = RandomForestClassifier()
    # Dummy training data
    X = np.array([[1, 20, 300], [2, 5, 1000], [5, 1, 500]])
    y = [0, 1, 1]  # 0: Not Fraud, 1: Fraud
    model.fit(X, y)

    # Features: [booking_count, time_gap_in_minutes, amount]
    prediction = model.predict([features])
    return prediction[0]
