"""
kRPC client module. The all point of this is to manage the connection to kRPC, from connection parameters.


"""

import krpc
from src.utils.logger import logD, logE
from utils.krapp_errors import KrappErrorConnection

# Default connection parameters
DEFAULT_IP = '127.0.0.1'
DEFAULT_RPC_PORT = 50000
DEFAULT_STREAM_PORT = 50001
DEFAULT_NAME = 'KrApp'


class _Client:
    client: krpc.client.Client

    def connect(self, ip: str = DEFAULT_IP, rpc_port: int = DEFAULT_RPC_PORT, stream_port: int = DEFAULT_STREAM_PORT,
                name: str = DEFAULT_NAME) -> None:
        """ Used to connect to a running kRPC server in KSP, using TCP/IP protocol.

        :param ip: IP address of the server on the local network
        :param rpc_port: RPC port
        :param stream_port: stream port
        :param name: Name of this client for the server
        """
        try:
            logD('Trying to connect to kRPC with parameters:')
            logD('name: "' + name + '" address: ' + ip + ' rpc port: ' + str(rpc_port) + ' stream port: ' +
                 str(stream_port))
            self.client = krpc.connect(name, ip, rpc_port, stream_port)
        except krpc.ConnectionError as error:
            raise KrappErrorConnection('kRPC connection error!')
        except Exception:  # Dirty but the only safe way I found not to crash the app
            raise KrappErrorConnection('Unhandled connection error (probably from OS)!')


_instance = _Client.client

"""To connect, use this first!"""
connect = _Client.connect

"""Attributes to get access to the game via kRPC services"""
krpc_service = _instance.krpc
space_center_service = _instance.space_center
