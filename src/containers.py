import dependency_injector.containers as containers
import dependency_injector.providers as providers

from src.utils.logger import KrappLogger


class Core(containers.DeclarativeContainer):
    logger = providers.Singleton(KrappLogger)