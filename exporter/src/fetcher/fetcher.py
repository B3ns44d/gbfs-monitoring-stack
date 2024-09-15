import logging
import time
from typing import Optional, Dict

import requests


class DataFetcher:
    def __init__(self, provider_name: str, auto_discovery_url: str, cache_duration: int = 60):
        self.provider_name = provider_name
        self.auto_discovery_url = auto_discovery_url
        self.cache_duration = cache_duration  # in seconds
        self.cache = None
        self.cache_timestamp = 0

    def fetch_provider_data(self) -> Optional[Dict]:
        """Fetches data from the GBFS provider's auto-discovery URL with caching."""
        current_time = time.time()
        if self.cache and (current_time - self.cache_timestamp) < self.cache_duration:
            logging.info(f"Using cached data for {self.provider_name}")
            return self.cache

        try:
            response = requests.get(self.auto_discovery_url, timeout=10)
            if response.status_code != 200:
                logging.error(f"Failed to fetch auto-discovery for {self.provider_name}: HTTP {response.status_code}")
                return None

            auto_discovery = response.json()
            feeds = auto_discovery.get('data', {}).get('en', {}).get('feeds', [])

            # Extract required feeds
            station_information_url = next((feed['url'] for feed in feeds if feed['name'] == 'station_information'),
                                           None)
            station_status_url = next((feed['url'] for feed in feeds if feed['name'] == 'station_status'), None)

            if not station_information_url or not station_status_url:
                logging.error(f"Missing required feeds for {self.provider_name}")
                return None

            # Fetch station information
            station_info_response = requests.get(station_information_url, timeout=10)
            if station_info_response.status_code != 200:
                logging.error(
                    f"Failed to fetch station information for {self.provider_name}: HTTP {station_info_response.status_code}")
                return None

            station_status_response = requests.get(station_status_url, timeout=10)
            if station_status_response.status_code != 200:
                logging.error(
                    f"Failed to fetch station status for {self.provider_name}: HTTP {station_status_response.status_code}")
                return None

            data = {
                'provider': self.provider_name,
                'station_information': station_info_response.json(),
                'station_status': station_status_response.json()
            }

            # Update cache
            self.cache = data
            self.cache_timestamp = current_time

            return data

        except requests.RequestException as e:
            logging.error(f"Error fetching data for {self.provider_name}: {e}")
            return None
