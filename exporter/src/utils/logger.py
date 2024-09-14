import logging


class LoggerSetup:
    @staticmethod
    def setup_logging():
        """
        Set up the logging configuration.
        """
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s - %(message)s',
        )
