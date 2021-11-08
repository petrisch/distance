# -*- coding: utf-8 -*-

# The ui handling part

import gi
from gi.repository import GLib, Gtk
gi.require_version('Gtk', '4.0')

# TODO: Remove this whole Template thing since there is no such thing!

@GtkTemplate(ui='src/distance_window.ui')
class DistanceWindow(Gtk.Box):

    print("Loading GUI from Template")

    __gtype_name__ = 'DistanceWindow'
    measure_button1 = GtkTemplate.Child()
    Labelbox = GtkTemplate.Child()
    SaveCSV_Button = GtkTemplate.Child()
    distance1_label3 = GtkTemplate.Child()

    print("Loaded GUI elements")

    def __init__(self):
        # super(Gtk.Box, self).__init__()
        print("Initializing GUI")
        super().__init__()
        self.init_template()
        # self.measure_button1.clicked()

    @GtkTemplate.Callback
    def measure_button1_clicked_cb(self, widget):
        distance = measure_distance(self)
        print("The distance is:" + str(distance))
        self.distance1_label3.set_markup(
                             _('<span size="large">Distance 1 is:'
                                 + str(distance) + '</span>'))

        # def  measure_button = self.get_object("measure_button")
        # measure_button.connect("clicked", self.measure_button_clicked_cb)
        # distance1_label = self.get_object("distance1_label")


def measure_distance(self):

    # The submodule for the BOSCH devices.
    # Has to be done that way because of the "-" in the Name

    import importlib
    rangefinder = importlib.import_module("BOSCH-GLM-rangefinder.glm100c")
    print("rangefinder loaded in window as: " + str(rangefinder))

    try:
        print("Initializing GLM50C")
        glm50c = rangefinder.GLM50C()
        if not glm50c.connected:
            distance = "No Connection"
            return distance
        distance = glm50c.measure_from_tripod_socket(glm50c)
        if distance != -1:
            return distance
        else:
            distance = "No value measured"

    except OSError:
        print("No Device connected")
        distance = "OS error"
        return distance
    except ConnectionError:
        print("No Connection posible")
        distance = "Connection Error"
        return
