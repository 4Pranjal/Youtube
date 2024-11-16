import os
import yaml

def load_config(config_path="./config/config.yaml"):
    """Load configuration from a YAML file."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def ensure_dir(path):
    """Ensure the directory exists."""
    os.makedirs(path, exist_ok=True)
