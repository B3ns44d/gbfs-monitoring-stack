import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

from fetcher.fetcher import DataFetcher
from metrics.metrics_manager import MetricsManager


class GBFSCollector:
    def __init__(self, providers: List[Dict[str, str]]):
        self.providers = providers
        self.metrics_manager = MetricsManager()
        self.data_fetchers = [
            DataFetcher(provider['name'], provider['auto_discovery_url'])
            for provider in self.providers
        ]
        self.initialized = False

    def collect(self):
        """This method is called by Prometheus to collect the metrics."""
        try:
            if not self.initialized:
                self.initialized = True

            # Use ThreadPoolExecutor to fetch data concurrently from all providers
            with ThreadPoolExecutor(max_workers=len(self.data_fetchers)) as executor:
                future_to_fetcher = {
                    executor.submit(self.process_provider, fetcher): fetcher
                    for fetcher in self.data_fetchers
                }
                for future in as_completed(future_to_fetcher):
                    fetcher = future_to_fetcher[future]
                    try:
                        future.result()
                    except Exception as exc:
                        logging.error(f"Provider {fetcher.provider_name} generated an exception: {exc}")

            # Yield all metrics
            yield from self.metrics_manager.collect()

        except Exception as e:
            logging.error(f"Error during data fetching: {e}")

    def process_provider(self, fetcher: DataFetcher):
        """Fetches data for a single provider and updates the metrics."""
        try:
            result = fetcher.fetch_provider_data()

            # Skip if no data is returned (e.g., missing required feeds)
            if not result:
                logging.warning(f"Skipping provider {fetcher.provider_name} due to missing data.")
                return

            provider_name = result.get('provider', 'unknown_provider')
            station_info_raw = result.get('station_information', {})
            station_status_raw = result.get('station_status', {})

            # Process and update the metrics
            self.metrics_manager.update_metrics(provider_name, station_info_raw, station_status_raw)

        except Exception as e:
            logging.error(f"Error processing provider {fetcher.provider_name}: {e}")
