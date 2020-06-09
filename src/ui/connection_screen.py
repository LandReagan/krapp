from containers import Core
from utils.observer import Observer
from utils.client_snapshot import ClientSnapshot
from utils.krapp_errors import *
from utils.logger import logger

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

Builder.load_file('ui/connection_screen.kv')


class ConnectionScreenMeta(type(Screen), type(Observer)):
    """To solve a metaclass error that I don't understand"""
    pass


class ConnectionScreen(Screen, Observer, metaclass=ConnectionScreenMeta):
    """
    Widget of kRPC connection parameters. It gets ip and ports information to
    connect through the client object.
    """
    # Widget linked properties
    connect_button = ObjectProperty(None)
    ip_input = ObjectProperty(None)
    rpc_port_input = ObjectProperty(None)
    stream_port_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt):
        Core.client().add_observer(self)  # Register as observer

    def krpc_connect(self):
        logger.info('Connecting to KSP...')
        try:
            Core.client().connect(ip=self.ip_input.text,
                                  rpc_port=int(self.rpc_port_input.text),
                                  stream_port=int(self.stream_port_input.text))
        except (KrappErrorOSConnection, KrappErrorConnection):
            ErrorPopup().open()

    def update(self, data: any) -> None:
        """
        Implementation of update() from Observer class.
        => Client will send ClientSnapshot
        :param data: any, see above
        """
        if isinstance(data, ClientSnapshot):
            if data.connection_status == 'CONNECTED':
                self.connect_button.text = 'DISCONNECT'
            else:
                self.connect_button.text = 'CONNECT'



class ErrorPopup(Popup):
    """
    Popup on error. See related KV file.
    """
    pass
