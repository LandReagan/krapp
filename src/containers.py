import dependency_injector.containers as containers
import dependency_injector.providers as providers

import connection.client


class Core(containers.DeclarativeContainer):
    client = providers.Singleton(connection.client.Client)
