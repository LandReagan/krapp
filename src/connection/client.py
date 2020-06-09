"""
kRPC client module. The all point of this is to manage the connection to
kRPC, from connection parameters.
"""
from typing import List

import krpc
from utils.logger import logger
from utils.krapp_errors import *
from utils.observer import Observable, Observer
from utils.client_snapshot import ClientSnapshot

# Default connection parameters
DEFAULT_IP = '127.0.0.1'
DEFAULT_RPC_PORT = 50000
DEFAULT_STREAM_PORT = 50001
DEFAULT_NAME = 'KrApp'


class Client(Observable):

    client: krpc.client.Client = None

    krpc_version: str = krpc.version.__version__
    connection_status: str = 'DISCONNECTED'
    body_name: str = '?'
    vessel_name: str = '?'

    _observers: List[Observer] = []

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
        self.notify_observers()

        try:
            logger.debug(
                'Trying to connect to kRPC with parameters:')
            logger.debug(
                'name: "' + name + '" address: ' + ip + ' rpc port: ' +
                str(rpc_port) + ' stream port: ' + str(stream_port))
            self.client = krpc.connect(name, ip, rpc_port, stream_port)
            self.connection_status = 'CONNECTED'
            self.notify_observers()
            self.start_game_scene_stream()

        except krpc.ConnectionError as error:
            self.connection_status = 'ERROR'
            self.notify_observers()
            logger.error('kRPC connection error!')
            raise KrappErrorConnection()

        except OSError:  # Would raise in case of wrong parameters, firewall...
            self.connection_status = 'ERROR'
            self.notify_observers()
            logger.error('OS connection error!')
            raise KrappErrorOSConnection()

    # Observable methods implementation
    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)
        self.notify_observers()

    def remove_observer(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:  # observer not found, disregard!
            pass

    def notify_observers(self) -> None:
        snapshot = ClientSnapshot(
            self.krpc_version,
            self.connection_status,
            self.body_name,
            self.vessel_name
        )
        logger.debug('Client notifies:\n' + str(snapshot))
        for observer in self._observers:
            observer.update(snapshot)

    def start_game_scene_stream(self):
        if self.connection_status == 'CONNECTED':
            game_scene_stream = self.client.add_stream(getattr,
                self.client.krpc, 'current_game_scene')
            game_scene_stream.add_callback(self.game_scene_change_callback)
            game_scene_stream.start()

    def game_scene_change_callback(self, game_scene):
        if not isinstance(game_scene, krpc.error.RPCError):
            logger.debug(game_scene)
            if 'flight' in str(game_scene):
                self.vessel_name = self.client.space_center.active_vessel.name
                self.body_name = self.client.space_center.active_vessel.orbit.body.name
            else:
                self.vessel_name = '?'
                self.body_name = '?'
        else:
            logger.error(str(game_scene))
        self.notify_observers()

    def stage(self):
        if self.client is not None:
            self.client.space_center.active_vessel.control\
                .activate_next_stage()
