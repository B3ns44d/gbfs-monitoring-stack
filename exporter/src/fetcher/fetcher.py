import logging
from threading import Lock
from typing import Dict, Any

import requests

from discovery import GBFSDiscovery


class DataFetcher:
    def __init__(self, provider_name: str, auto_discovery_url: str):
        self.provider_name = provider_name
        self.auto_discovery_url = auto_discovery_url
        self.feed_urls = {}
        self.session = requests.Session()
        self.initialized = False
        self.lock = Lock()

    def initialize(self):
        """Initialize the fetcher by fetching the feed URLs."""
        with self.lock:
            if not self.initialized:
                discovery = GBFSDiscovery(self.auto_discovery_url)
                self.feed_urls = discovery.fetch_feed_urls(self.session)

                if not self.feed_urls:
                    logging.error(f"Skipping provider {self.provider_name} due to missing required feeds.")
                    self.initialized = False
                else:
                    self.initialized = True

    def fetch_feed_data(self, url: str) -> Dict[str, Any]:
        try:
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            logging.error(f"Timeout fetching data from {url}")
            raise
        except Exception as e:
            logging.error(f"Error fetching data from {url}: {e}")
            raise

    def fetch_provider_data(self) -> Dict[str, Any]:
        """Fetch station information and status data for the provider."""
        if not self.initialized:
            logging.warning(f"Provider {self.provider_name} is not initialized due to missing feeds.")
            return {}

        # Check if 'station_information' and 'station_status' feeds exist
        if 'station_information' not in self.feed_urls or 'station_status' not in self.feed_urls:
            logging.error(
                f"Provider {self.provider_name} is missing required feeds ('station_information' or "
                f"'station_status'). Skipping...")
            return {}

        station_info_data = self.fetch_feed_data(self.feed_urls['station_information'])
        station_status_data = self.fetch_feed_data(self.feed_urls['station_status'])

        return {
            'provider': self.provider_name,
            'station_information': station_info_data,
            'station_status': station_status_data
        }
