import pymc3 as pm
import numpy as np
import logging
from src.utils.logging import logger

def bayesian_model(data):
    with pm.Model() as model:
        # Define priors
        alpha = pm.Normal('alpha', mu=0, sigma=10)
        beta = pm.Normal('beta', mu=0, sigma=10, shape=(len(data.columns) - 1))
        
        # Likelihood function
        mu = alpha + pm.math.dot(data.iloc[:, :-1], beta)
        sigma = pm.HalfNormal('sigma', sigma=1)
        
        likelihood = pm.Normal('likelihood', mu=mu, sigma=sigma, observed=data.iloc[:, -1])
        
        # Sample posterior
        trace = pm.sample(config['model']['bayesian']['num_samples'], chains=config['model']['bayesian']['chains'])
        
        logger.info("Bayesian model successfully trained.")
        
        return trace
