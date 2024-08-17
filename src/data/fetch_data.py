import requests
import logging
from src.config.config import load_config
from src.utils.logging import logger

config = load_config()

def fetch_nba_data(endpoint):
    url = f"{config['api']['base_url']}/{endpoint}"
    headers = {"Authorization": f"Bearer {config['secrets']['api_key']}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Data fetched from {url}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch data: {e}")
        return None
print(config)
