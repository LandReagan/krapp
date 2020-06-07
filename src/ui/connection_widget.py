from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang.builder import Builder

from containers import Core
from utils.krapp_errors import *

Builder.load_file('ui/connection_widget.kv')


class ConnectionWidget(BoxLayout):
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
        BoxLayout.__init__(self, **kwargs)
        self._client = Core.client()

    def krpc_connect(self):
        Core.logger().info('Connecting to KSP...')
        try:
            self._client.connect(ip=self.ip_input.text,
                                 rpc_port=int(self.rpc_port_input.text),
                                 stream_port=int(self.stream_port_input.text))
        except (KrappErrorOSConnection, KrappErrorConnection):
            ErrorPopup().open()


class ErrorPopup(Popup):
    """
    Popup on error. See related KV file.
    """
    pass
