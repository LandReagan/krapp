from containers import Core

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('ui/basic_controls_screen.kv')


class BasicControlsScreen(Screen):
    """

    """

    altitude_label = ObjectProperty(None)
    stage_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)

    def stage(self):
        Core.client().stage()
