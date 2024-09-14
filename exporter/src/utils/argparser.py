import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="GBFS Prometheus Exporter: Collects metrics from GBFS providers and exposes them for Prometheus."
    )
    parser.add_argument(
        '-c', '--config',
        type=str,
        default='../configs/providers.yaml',
        help='Path to the configuration file (default: configs/providers.yaml)'
    )
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=8000,
        help='Port to expose metrics on (default: 8000)'
    )
    return parser.parse_args()
