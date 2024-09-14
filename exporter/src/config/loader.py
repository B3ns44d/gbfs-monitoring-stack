import os
from typing import List, Dict

import yaml


class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.providers = self.load_providers_config()

    def load_providers_config(self) -> List[Dict[str, str]]:
        """
        Load the providers configuration from a YAML file.

        :return: A list of provider configurations.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found at: {self.config_path}")

        with open(self.config_path, 'r') as file:
            config = yaml.safe_load(file)

        providers = config.get('providers')
        if not providers:
            raise ValueError("No providers found in the configuration file.")

        return providers
