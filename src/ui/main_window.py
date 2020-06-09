from utils.logger import logger

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

Builder.load_file('ui/main_window.kv')


class MainWindow(BoxLayout):
    """
    The main window has a title and a navigator bar at the top, its content on the middle,
    and a status bar at the bottom.

    It is responsible for the orientation of the UI
    """

    status_bar = ObjectProperty(None)
    navigation_bar = ObjectProperty(None)
    screen_manager = ObjectProperty(None)

    screen_orientation = StringProperty('landscape')

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.on_size_changed()  # to set the correct size
        Clock.schedule_once(self.initialize)

    def initialize(self, dt):
        self.screen_manager.transition = NoTransition()
        self.navigation_bar.screen_manager = self.screen_manager

    def on_size_changed(self):
        if self.width > self.height:
            self.screen_orientation = 'landscape'
        else:
            self.screen_orientation = 'portrait'

    def on_screen_orientation(self, *args):
        if self.screen_orientation == 'landscape':
            self.status_bar.orientation = 'horizontal'
            self.status_bar.height = 30
        else:
            self.status_bar.orientation = 'vertical'
            self.status_bar.height = 60
