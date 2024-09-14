import logging

from prometheus_client.core import GaugeMetricFamily

from . import metrics_definitions as md


class MetricsManager:
    def __init__(self):
        self.metrics = md

    def update_metrics(
            self, provider_name: str, station_info_raw: dict, station_status_raw: dict
    ):
        """Updates Prometheus metrics based on the fetched data."""
        logging.debug(f"Updating metrics for provider: {provider_name}")

        # Clear previous samples to avoid accumulation
        for metric in self.metrics.__dict__.values():
            if isinstance(metric, GaugeMetricFamily):
                metric.samples.clear()

        # Parse the raw data
        station_info_list = station_info_raw.get('data', {}).get('stations', [])
        station_status_list = station_status_raw.get('data', {}).get('stations', [])

        total_bikes_available = 0
        total_docks_available = 0
        total_bikes_disabled = 0
        total_docks_disabled = 0
        total_stations = len(station_info_list)
        total_active_stations = 0
        total_bikes_in_use = 0

        station_info_dict = {station['station_id']: station for station in station_info_list}

        # Update metrics for each station
        for status in station_status_list:
            station_id = status['station_id']
            info = station_info_dict.get(station_id)

            if not info:
                logging.warning(f"Station information missing for station_id: {station_id}")
                continue

            lat = info.get('lat', 0)
            lon = info.get('lon', 0)
            labels = [provider_name, station_id, info['name'], str(lat), str(lon)]

            # Get status data
            num_bikes_available = status.get('num_bikes_available', 0)
            num_docks_available = status.get('num_docks_available', 0)
            num_bikes_disabled = status.get('num_bikes_disabled', 0)
            num_docks_disabled = status.get('num_docks_disabled', 0)
            is_installed = status.get('is_installed', 0)
            is_renting = status.get('is_renting', 0)
            is_returning = status.get('is_returning', 0)
            capacity = info.get('capacity', 0)

            # Compute bikes in use
            bikes_in_use = capacity - num_bikes_available
            total_bikes_in_use += bikes_in_use

            # Update station-level metrics
            self.metrics.gbfs_bikes_available.add_metric(labels, num_bikes_available)
            self.metrics.gbfs_docks_available.add_metric(labels, num_docks_available)
            self.metrics.gbfs_bikes_disabled.add_metric(labels, num_bikes_disabled)
            self.metrics.gbfs_docks_disabled.add_metric(labels, num_docks_disabled)
            self.metrics.gbfs_station_capacity.add_metric(labels, capacity)
            self.metrics.gbfs_station_is_installed.add_metric(labels, is_installed)
            self.metrics.gbfs_station_is_renting.add_metric(labels, is_renting)
            self.metrics.gbfs_station_is_returning.add_metric(labels, is_returning)
            self.metrics.gbfs_bikes_in_use.add_metric(labels, bikes_in_use)

            # Update num_bikes_available_types if exists
            num_bikes_available_types = status.get('num_bikes_available_types', {})
            if num_bikes_available_types:
                for bike_type, count in num_bikes_available_types.items():
                    type_labels = labels + [bike_type]
                    self.metrics.gbfs_num_bikes_available_types.add_metric(type_labels, count)

            # Accumulate totals
            total_bikes_available += num_bikes_available
            total_docks_available += num_docks_available
            total_bikes_disabled += num_bikes_disabled
            total_docks_disabled += num_docks_disabled

            if is_installed and is_renting and is_returning:
                total_active_stations += 1

        # Update overall metrics for the provider
        self.metrics.gbfs_bikes_available_total.add_metric([provider_name], total_bikes_available)
        self.metrics.gbfs_docks_available_total.add_metric([provider_name], total_docks_available)
        self.metrics.gbfs_bikes_disabled_total.add_metric([provider_name], total_bikes_disabled)
        self.metrics.gbfs_docks_disabled_total.add_metric([provider_name], total_docks_disabled)
        self.metrics.gbfs_active_stations_total.add_metric([provider_name], total_active_stations)
        self.metrics.gbfs_stations_total.add_metric([provider_name], total_stations)
        self.metrics.gbfs_bikes_in_use_total.add_metric([provider_name], total_bikes_in_use)

        logging.info(f"Metrics updated for provider: {provider_name}")

    def collect(self):
        """Yields the metrics to Prometheus."""
        # Yield all metrics that were updated
        for metric in self.metrics.__dict__.values():
            if isinstance(metric, GaugeMetricFamily):
                yield metric
