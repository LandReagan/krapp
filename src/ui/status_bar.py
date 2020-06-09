from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

from containers import Core
from utils.client_snapshot import ClientSnapshot
from utils.observer import Observer

Builder.load_file('ui/status_bar.kv')


class StatusBarMeta(type(BoxLayout), type(Observer)):
    pass


class StatusBar(BoxLayout, Observer, metaclass=StatusBarMeta):

    krpc_version_label = ObjectProperty()
    ksp_status_label = ObjectProperty()
    body_name_label = ObjectProperty()
    vessel_name_label = ObjectProperty()

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt):
        Core.client().add_observer(self)

    def update(self, data: any) -> None:
        if isinstance(data, ClientSnapshot):

            self.krpc_version_label.text = data.krpc_version
            
            if data.connection_status == 'DISCONNECTED':
                self.ksp_status_label.text = 'DISC'
                self.ksp_status_label.color = (223/255, 105/255, 17/255, 1)
            elif data.connection_status == 'CONNECTED':
                self.ksp_status_label.text = 'CONN'
                self.ksp_status_label.color = (0.1, 1, 0.1, 1)
            elif data.connection_status == 'ERROR':
                self.ksp_status_label.text = 'ERR'
                self.ksp_status_label.color = (0.9, 0.1, 0, 1)

            self.body_name_label.text = data.body_name
            self.vessel_name_label.text = data.vessel_name


