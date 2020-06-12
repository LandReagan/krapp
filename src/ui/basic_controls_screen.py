from containers import Core

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

Builder.load_file('ui/basic_controls_screen.kv')


class BasicControlsScreen(Screen):
    """

    """

    altitude_label = ObjectProperty(None)
    stage_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

    def on_enter(self, *args):
        Screen.on_enter(self, *args)
        Core.client().add_altitude_callback(self.update_altitude)

    def update_altitude(self, altitude: int):
        self.altitude_label.text = str(altitude)

    def stage(self):
        Core.client().stage()
