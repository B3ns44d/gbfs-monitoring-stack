import logging
from typing import Dict

import requests


class GBFSDiscovery:
    def __init__(self, auto_discovery_url: str):
        self.auto_discovery_url = auto_discovery_url
        self.feed_urls = {}

    def fetch_feed_urls(self, session: requests.Session) -> Dict[str, str]:
        """Fetch the auto-discovery URL and extract feed URLs."""
        try:
            response = session.get(self.auto_discovery_url)
            response.raise_for_status()
            data = response.json()

            feeds_data = data.get('data')
            if not feeds_data:
                logging.error(f"No 'data' key in auto-discovery feed from {self.auto_discovery_url}")
                raise ValueError("Invalid auto-discovery feed format.")

            feeds = []
            for lang in feeds_data.keys():
                feeds.extend(feeds_data[lang]['feeds'])

            # Extract only required feeds
            self.feed_urls = {
                feed['name']: feed['url']
                for feed in feeds
                if feed['name'] in ['station_information', 'station_status']
            }

            # If required feeds are missing, log and return empty feed URLs
            if 'station_information' not in self.feed_urls or 'station_status' not in self.feed_urls:
                logging.error(f"Required feeds missing in auto-discovery feed from {self.auto_discovery_url}")
                return {}

            return self.feed_urls
        except Exception as e:
            logging.error(f"Error fetching auto-discovery feed from {self.auto_discovery_url}: {e}")
            raise
