from prometheus_client.core import GaugeMetricFamily

# 1. Total Bikes Available
gbfs_bikes_available_total = GaugeMetricFamily(
    'gbfs_bikes_available_total',
    'Total number of bikes available',
    labels=['provider']
)

# 2. Total Docks Available
gbfs_docks_available_total = GaugeMetricFamily(
    'gbfs_docks_available_total',
    'Total number of docks available',
    labels=['provider']
)

# 3. Bikes Available per Station
gbfs_bikes_available = GaugeMetricFamily(
    'gbfs_bikes_available',
    'Number of bikes available at each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 4. Docks Available per Station
gbfs_docks_available = GaugeMetricFamily(
    'gbfs_docks_available',
    'Number of docks available at each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 5. Total Bikes Disabled
gbfs_bikes_disabled_total = GaugeMetricFamily(
    'gbfs_bikes_disabled_total',
    'Total number of bikes disabled',
    labels=['provider']
)

# 6. Bikes Disabled per Station
gbfs_bikes_disabled = GaugeMetricFamily(
    'gbfs_bikes_disabled',
    'Number of bikes disabled at each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 7. Total Docks Disabled
gbfs_docks_disabled_total = GaugeMetricFamily(
    'gbfs_docks_disabled_total',
    'Total number of docks disabled',
    labels=['provider']
)

# 8. Docks Disabled per Station
gbfs_docks_disabled = GaugeMetricFamily(
    'gbfs_docks_disabled',
    'Number of docks disabled at each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 9. Total Active Stations
gbfs_active_stations_total = GaugeMetricFamily(
    'gbfs_active_stations_total',
    'Total number of active stations',
    labels=['provider']
)

# 10. Total Stations
gbfs_stations_total = GaugeMetricFamily(
    'gbfs_stations_total',
    'Total number of stations',
    labels=['provider']
)

# 11. Station Capacity
gbfs_station_capacity = GaugeMetricFamily(
    'gbfs_station_capacity',
    'Capacity of each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 12. Station Status Flags
gbfs_station_is_installed = GaugeMetricFamily(
    'gbfs_station_is_installed',
    'Whether the station is installed',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

gbfs_station_is_renting = GaugeMetricFamily(
    'gbfs_station_is_renting',
    'Whether the station is renting bikes',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

gbfs_station_is_returning = GaugeMetricFamily(
    'gbfs_station_is_returning',
    'Whether the station is accepting bike returns',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 13. Bikes in Use per Station
gbfs_bikes_in_use = GaugeMetricFamily(
    'gbfs_bikes_in_use',
    'Number of bikes currently in use at each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon']
)

# 14. Total Bikes in Use
gbfs_bikes_in_use_total = GaugeMetricFamily(
    'gbfs_bikes_in_use_total',
    'Total number of bikes currently in use',
    labels=['provider']
)

# 15. Bikes Available by Type
gbfs_num_bikes_available_types = GaugeMetricFamily(
    'gbfs_num_bikes_available_types',
    'Number of bikes available by type at each station',
    labels=['provider', 'station_id', 'station_name', 'lat', 'lon', 'bike_type']
)
