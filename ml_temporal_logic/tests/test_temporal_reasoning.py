from ml_temporal_logic.pyreason_integration.temporal_reasoning import TemporalReasoner

def test_reasoning_output():
    reasoner = TemporalReasoner()
    mock_preds = [1, 2, 3]
    results = reasoner.run_reasoning(mock_preds)
    assert all(res["logic_outcome"] for res in results.values())
    print("All tests passed!")

if __name__ == "__main__":
    test_reasoning_output()
