from collections import defaultdict
import time
import joblib
import numpy as np

# Track requests per IP
request_counts = defaultdict(list)

# Load ML model
try:
    model = joblib.load("models/ddos_model.pkl")
except:
    model = None

def analyze_request(ip):
    now = time.time()
    request_counts[ip].append(now)

    # Keep only last 10 seconds
    request_counts[ip] = [t for t in request_counts[ip] if now - t < 10]

    count = len(request_counts[ip])
    features = [count, len(request_counts)]
    attack = False

    # Rule-based check
    if count > 50:  # 50 requests in 10 sec
        attack = True

    # ML-based check
    if model:
        pred = model.predict([features])
        if pred[0] == -1:
            attack = True

    return {"attack": attack, "count": count}
