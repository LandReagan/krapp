import krpc
from utils.logger import logD, logE


class Client:
    connection: krpc.client.Client = None
    vessel = None

    def connect(
            self,
            name: str = 'NO NAME',
            address: str = '127.0.0.1',
            rpc_port: int = 1000,
            stream_port: int = 1001
    ) -> None:
        try:
            logD('Trying to connect to kRPC with parameters:')
            logD('name: "' + name + '" address: ' + address + ' rpc port: ' + str(rpc_port) + ' stream port: ' +
                 str(stream_port))
            self.connection = krpc.connect(name, address, rpc_port, stream_port)
        except krpc.ConnectionError as error:
            logE('Connection ERROR! Error: ' + str(error))
        except:  # Dirty but the only safe way I found not to crash the app
            logE('Unhandled exception happened!')
