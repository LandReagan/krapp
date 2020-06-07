from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

from containers import Core

Builder.load_file('ui/status_bar.kv')


class StatusBar(BoxLayout):

    krpc_version_label = ObjectProperty()
    ksp_status_label = ObjectProperty()
    body_name_label = ObjectProperty()
    vessel_name_label = ObjectProperty()

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.client = Core.client()
        Clock.schedule_once(self.build)

    def build(self, dt):
        if self.client.connection_status == 'DISCONNECTED':
            self.ksp_status_label.text = 'DISC'
            self.ksp_status_label.color = (223/255, 105/255, 17/255, 1)
        elif self.client.connection_status == 'DISCONNECTED':
            self.ksp_status_label.text = 'CONN'
            self.ksp_status_label.color = (0.1, 1, 0.1, 1)
        elif self.client.connection_status == 'ERROR':
            self.ksp_status_label.text = 'ERR'
            self.ksp_status_label.color = (0.9, 0.1, 0, 1)


