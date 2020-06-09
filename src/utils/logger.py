import logging


class KrappLogger:

    def __init__(self) -> None:
        self.logger = logging.getLogger('main_logger')
        self.logger.setLevel(logging.DEBUG)

        # Set console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # My formatter
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s: %(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

        self.logger.info('Logger started!')

    def stop(self) -> None:
        self.logger.info('App stops!')

    def debug(self, message: str = "") -> None:
        self.logger.debug(message)

    def info(self, message: str = "") -> None:
        self.logger.info(message)

    def warn(self, message: str = "") -> None:
        self.logger.warning(message)

    def error(self, message: str = "") -> None:
        self.logger.error(message)

    def critical(self, message: str = "") -> None:
        self.logger.critical(message)


logger = KrappLogger()
