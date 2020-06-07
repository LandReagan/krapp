import dependency_injector.containers as containers
import dependency_injector.providers as providers

from utils.logger import KrappLogger
import connection.client


class Core(containers.DeclarativeContainer):
    logger = providers.Singleton(KrappLogger)

    client = providers.Singleton(connection.client.Client)
