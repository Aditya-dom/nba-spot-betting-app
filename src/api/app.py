from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import src.models.bayesian_model as bayesian_model
import src.models.monte_carlo as monte_carlo

app = FastAPI()

class PredictionRequest(BaseModel):
    home_team: str
    away_team: str

@app.post("/predict")
def predict_outcome(request: PredictionRequest):
    try:
        # Dummy team strengths (In practice, get this from Bayesian model or DB)
        team_strengths = {'home': 1.2, 'away': 0.8}
        probability = monte_carlo.monte_carlo_simulation(team_strengths)
        return {"home_team_win_probability": probability}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
