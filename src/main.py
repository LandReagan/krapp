import krpc
from containers import Core

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MainWindow(BoxLayout):

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)


class StatusBar(BoxLayout):

    kRPC_version_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        Clock.schedule_once(self.initialize)

    def initialize(self, dt):
        self.kRPC_version_label.text = 'kRPC: v' + krpc.version.__version__


class KRPCApp(App):
    def build(self):
        self.title = 'kRPC tester'
        return MainWindow()


if __name__ == '__main__':
    Core.logger().info('App is starting!')
    KRPCApp().run()
