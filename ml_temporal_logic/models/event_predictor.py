import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

class EventPredictor:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.encoder = LabelEncoder()

    def train(self, df: pd.DataFrame):
        X = self.encoder.fit_transform(df['event_type']).reshape(-1, 1)
        y = df['event_id']
        self.model.fit(X, y)

    def predict(self, df: pd.DataFrame):
        X = self.encoder.transform(df['event_type']).reshape(-1, 1)
        return self.model.predict(X)
