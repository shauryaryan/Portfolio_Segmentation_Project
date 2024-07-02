from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    iso_forest = IsolationForest(contamination=0.1)
    iso_forest.fit(data)
    return iso_forest.predict(data)
