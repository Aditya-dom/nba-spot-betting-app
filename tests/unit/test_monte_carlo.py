from src.models.monte_carlo import monte_carlo_simulation

def test_monte_carlo_simulation():
    team_strengths = {'home': 1.2, 'away': 0.8}
    probability = monte_carlo_simulation(team_strengths, num_simulations=1000)
    assert 0 <= probability <= 1
