from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={"home_team": "Lakers", "away_team": "Warriors"})
    assert response.status_code == 200
    data = response.json()
    assert "home_team_win_probability" in data
