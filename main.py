# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
__version__ = '1.0'  # declare the app version. Will be used by buildozer

from kivy.app import App  # for the main app
from kivy.uix.floatlayout import FloatLayout  # the UI layout
from kivy.uix.label import Label  # a label to show information
from plyer import accelerometer  # object to read the accelerometer
from kivy.clock import Clock  # clock to schedule a method


class UI(FloatLayout):  # the app ui
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.lblAcce = Label(text="Accelerometer: ")  # create a label at the center
        self.add_widget(self.lblAcce)  # add the label at the screen
        try:
            accelerometer.enable()  # enable the accelerometer
            # if you want do disable it, just run: accelerometer.disable()
            Clock.schedule_interval(self.update, 1.0 / 24)  # 24 calls per second
        except:
            self.lblAcce.text = "Failed to start accelerometer"  # error

    def update(self, dt):
        txt = ""
        try:
            txt = "Accelerometer:\nX = %.2f\nY = %.2f\nZ = %2.f " % (
                accelerometer.acceleration[0],  # read the X value
                accelerometer.acceleration[1],  # Y
                accelerometer.acceleration[2])  # Z
        except:
            txt = "Cannot read accelerometer!"  # error
        self.lblAcce.text = txt  # add the correct text


class Accelerometer(App):  # our app
    def build(self):
        ui = UI()  # create the UI
        return ui  # show it


if __name__ == '__main__':
    Accelerometer().run()  # start our app