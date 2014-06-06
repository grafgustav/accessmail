import kivy

kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, VariableListProperty

from kivy.core.window import Window

from src.GUI.addressLayout import AddressLayout
from src.GUI.writeLayout import WriteLayout
from src.GUI.overviewLayout import OverviewLayout
from src.GUI.readLayout import ReadLayout
from src.GUI.menuLayout import MenuLayout


class MenuLayout(BoxLayout):
    pass


class Catalog(BoxLayout):

    def __init__(self, **kwargs):
        super(Catalog, self).__init__(**kwargs)
        screen_manager = ObjectProperty()
        buttons = VariableListProperty()
        self.current_butt = 0
        Window.bind(on_key_down=self.rotate_buttons)

    def show_layout(self, value):
        self.screen_manager.current = value
        return

    def rotate_buttons(self, keyboard, key,  *args):
        print("enter rotate button")
        print("current_butt: %d" %(self.current_butt))
        if key == 9:
            if self.current_butt < len(self.buttons)-1:
                self.current_butt += 1
            else:
                self.current_butt = 0
        if key == 13:
            print("Return pressed")
            self.buttons[self.current_butt].on_press()
        print("leaving rotate buttons")


class MainApp(App):
    def build(self):
        return Catalog()

if __name__ == "__main__":
    MainApp().run()