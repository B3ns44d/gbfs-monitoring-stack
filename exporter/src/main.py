import logging
import sys

from prometheus_client import start_http_server, REGISTRY

from collector import GBFSCollector
from config.loader import ConfigLoader
from utils.argparser import parse_args
from utils.logger import LoggerSetup


def main():
    args = parse_args()

    # Setup logging
    LoggerSetup.setup_logging()

    # Load configuration
    config_path = args.config
    try:
        config_loader = ConfigLoader(config_path)
        providers = config_loader.providers
    except Exception as e:
        logging.error(f"Failed to load configuration from {config_path}: {e}")
        sys.exit(1)

    logging.info("Setting up GBFS Prometheus Exporter.")

    # Initialize the GBFS collector
    collector = GBFSCollector(providers)
    REGISTRY.register(collector)

    # Start the Prometheus HTTP server
    try:
        start_http_server(args.port)
        logging.info(f"Exporter started and Prometheus metrics are exposed on port {args.port}.")
    except Exception as e:
        logging.error(f"Failed to start HTTP server on port {args.port}: {e}")
        sys.exit(1)

    import time
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Exporter is shutting down.")


if __name__ == '__main__':
    main()
