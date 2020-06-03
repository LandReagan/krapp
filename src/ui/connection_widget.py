from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang.builder import Builder

from utils.logger import logD, logI
from connection.client import Client

Builder.load_file('ui/connection_widget.kv')


class ConnectionWidget(BoxLayout):
    kRPC_CWB = ObjectProperty()
    connection_CWB = ObjectProperty()
    vessel_CWB = ObjectProperty()
    ksp_state: Client = None

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.ksp_state = Client()
        Clock.schedule_once(self.initialize)

    def initialize(self, dt) -> None:
        logD('ConnectionWidget initialization')
        self.kRPC_CWB.title = 'kRPC module'
        self.connection_CWB.title = 'KSP connection'
        self.vessel_CWB.title = 'Vessel connection'
        self.kRPC_CWB.lower_label.text = 'OK'


class ConnectionWidgetFlag(BoxLayout):
    
    title = StringProperty()
    upper_label = ObjectProperty()
    lower_label = ObjectProperty()

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt) -> None:
        self.upper_label.text = self.title


class ConnectionParameters(BoxLayout):
    
    start_button = ObjectProperty(None)
    ip_input = ObjectProperty(None)
    rpc_port_input = ObjectProperty(None)
    stream_port_input = ObjectProperty(None)
    ksp_state: Client = None

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt):
        pass

    def select_ip(self):
        self.ip_input.text = ''

    def krpc_connect(self):
        logI('Connecting to KSP...')
        if self.ksp_state is not None:
            self.ksp_state.connect()
        else:
            logD('Initialization problem! Connection stopped.')


