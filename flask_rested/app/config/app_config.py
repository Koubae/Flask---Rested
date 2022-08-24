from flask import Flask
import os
import sys
from dotenv import load_dotenv
from ..core.logger import create_logger

__version__ = '0.0.1'

def load_configs(app: Flask, base_dir: str) -> None:
    """Load Flask App Config

    Args:
        app (Flask):
        base_dir (str):

    Returns:
        None
    """
    env = os.environ.get('ENV', 'development')
    CONFIG_PATH = '.env.production' if env == 'production' else '.env'
    config_file = os.path.join(base_dir, 'config/', CONFIG_PATH)
    if not os.path.exists(config_file):
        print("Environment file missing, app shutting down...")
        sys.exit(1)
    load_dotenv(config_file)
    app.config.from_mapping(os.environ)

    # Add additional configs
    app.config['BASE_DIR'] = base_dir
    app.config['LOGGER'] = create_logger