from sklearn.ensemble import RandomForestClassifier

def classify_portfolio(data, labels):
    clf = RandomForestClassifier()
    clf.fit(data, labels)
    return clf
