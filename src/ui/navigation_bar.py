from utils.logger import logger

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('ui/navigation_bar.kv')


class NavigationBar(BoxLayout):
    """
    This widget stores the buttons for navigation between 'screen' widgets.
    To work properly, it needs a reference to the screen manager of the main
    window.
    """

    screen_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)

    def nav_to(self, screen_name: str):
        self.screen_manager.current = screen_name
