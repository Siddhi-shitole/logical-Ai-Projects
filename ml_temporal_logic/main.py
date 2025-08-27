import pandas as pd
from ml_temporal_logic.models.event_predictor import EventPredictor
from ml_temporal_logic.pyreason_integration.temporal_reasoning import TemporalReasoner

data = pd.read_csv('data/sample_temporal_events.csv')

predictor = EventPredictor()
predictor.train(data)

reasoner = TemporalReasoner()
predictions = predictor.predict(data)
results = reasoner.run_reasoning(predictions)

print("ML-Enhanced Temporal Logic Reasoning Results:")
for idx, res in results.items():
    print(res)
