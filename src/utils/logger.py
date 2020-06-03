import logging

logger = None


def init() -> None:
    # Create logger
    global logger
    logger = logging.getLogger('main_logger')
    logger.setLevel(logging.DEBUG)

    # Set console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # My formatter
    formatter = logging.Formatter('%(asctime)s | %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.info('Logger started!')


def stop() -> None:
    global logger
    logI('App stops!')


def logD(message: str = "") -> None:
    global logger
    logger.debug(message)


def logI(message: str = "") -> None:
    global logger
    logger.info(message)


def logW(message: str = "") -> None:
    global logger
    logger.warning(message)


def logE(message: str = "") -> None:
    global logger
    logger.error(message)


def logC(message: str = "") -> None:
    global logger
    logger.critical(message)
