import numpy as np
import logging
from src.utils.logging import logger

def monte_carlo_simulation(probabilities, num_simulations=10000):
    results = []
    for i in range(num_simulations):
        result = np.random.choice(['win', 'loss'], p=probabilities)
        results.append(result)
    
    win_percentage = results.count('win') / num_simulations
    logger.info(f"Monte Carlo Simulation Result: {win_percentage * 100}% win rate")
    return win_percentage
