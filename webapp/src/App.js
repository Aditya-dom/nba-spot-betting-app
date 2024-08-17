import React, { useState } from 'react';

function App() {
  const [homeTeam, setHomeTeam] = useState("");
  const [awayTeam, setAwayTeam] = useState("");
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ home_team: homeTeam, away_team: awayTeam }),
    });
    const data = await response.json();
    setPrediction(data.home_team_win_probability);
  };

  return (
    <div className="App">
      <h1>NBA Game Predictor</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Home Team" value={homeTeam} onChange={e => setHomeTeam(e.target.value)} />
        <input type="text" placeholder="Away Team" value={awayTeam} onChange={e => setAwayTeam(e.target.value)} />
        <button type="submit">Predict</button>
      </form>
      {prediction && <div>Win Probability: {prediction}</div>}
    </div>
  );
}

export default App;
