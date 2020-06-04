from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang.builder import Builder

from containers import Core

Builder.load_file('ui/connection_widget.kv')


class ConnectionWidget(BoxLayout):
    kRPC_CWB = ObjectProperty()
    connection_CWB = ObjectProperty()
    vessel_CWB = ObjectProperty()

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt) -> None:
        Core.logger().debug('ConnectionWidget initialization')
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

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt):
        pass

    def select_ip(self):
        self.ip_input.text = ''

    def krpc_connect(self):
        Core.logger().info('Connecting to KSP...')
        # todo


