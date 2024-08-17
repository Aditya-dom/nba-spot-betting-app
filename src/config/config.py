import yaml

def load_config(config_path='src/config/config.yaml', secrets_path='src/config/secrets.yaml'):
    """Load configuration from YAML files."""
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    
    with open(secrets_path, 'r') as secrets_file:
        secrets = yaml.safe_load(secrets_file)
    
    # Merge secrets into the config
    config['secrets'] = secrets
    return config
