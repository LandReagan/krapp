from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file('ui/title_bar.kv')


class TitleBar(BoxLayout):

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
