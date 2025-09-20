import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

def train_model():
    # Fake normal traffic samples: [requests_in_10s, unique_ips]
    X_train = np.array([
        [5, 20],
        [8, 22],
        [12, 18],
        [15, 25],
        [10, 19]
    ])

    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(X_train)

    joblib.dump(model, "models/ddos_model.pkl")
    print("ML model trained and saved!")

if __name__ == "__main__":
    train_model()
