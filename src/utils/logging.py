import logging.config
import yaml

def setup_logging(default_path='src/config/logging.yaml', default_level=logging.INFO):
    """Setup logging configuration."""
    with open(default_path, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Run this once when the application starts
setup_logging()
logger = logging.getLogger('app_logger')
