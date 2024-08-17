from pydantic import BaseModel

class PredictionRequest(BaseModel):
    home_team: str
    away_team: str
