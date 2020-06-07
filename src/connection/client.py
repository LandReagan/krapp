"""
kRPC client module. The all point of this is to manage the connection to
kRPC, from connection parameters.
"""

import enum

import krpc
import containers
import utils.krapp_errors

# Default connection parameters
DEFAULT_IP = '127.0.0.1'
DEFAULT_RPC_PORT = 50000
DEFAULT_STREAM_PORT = 50001
DEFAULT_NAME = 'KrApp'


class Client:

    client: krpc.client.Client
    connection_status: str = 'DISCONNECTED'
    krpc_version: str = krpc.version.__version__

    def connect(self,
                ip: str = DEFAULT_IP,
                rpc_port: int = DEFAULT_RPC_PORT,
                stream_port: int = DEFAULT_STREAM_PORT,
                name: str = DEFAULT_NAME) -> None:
        """
        Used to connect to a running kRPC server in KSP, using TCP/IP protocol.

        :param ip: IP address of the server on the local network
        :param rpc_port: RPC port
        :param stream_port: stream port
        :param name: Name of this client for the server
        """
        self.connection_status = 'WAITING'
        try:
            containers.Core.logger().debug(
                'Trying to connect to kRPC with parameters:')
            containers.Core.logger().debug(
                'name: "' + name + '" address: ' + ip + ' rpc port: ' +
                str(rpc_port) + ' stream port: ' + str(stream_port))
            self.client = krpc.connect(name, ip, rpc_port, stream_port)
            self.connection_status = 'CONNECTED'
        except krpc.ConnectionError as error:
            self.connection_status = 'ERROR'
            raise utils.krapp_errors.KrappErrorConnection()
        except OSError:  # Would raise in case of wrong parameters, firewall...
            self.connection_status = 'ERROR'
            raise utils.krapp_errors.KrappErrorOSConnection()

    @property
    def krpc(self):
        """
        To get the KRPC services
        :return:
        """
        return self.client.krpc

    @property
    def status(self):
        return self.connection_status
