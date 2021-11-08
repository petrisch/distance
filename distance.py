# -*- coding: utf-8 -*-

# The purpose of this is mainly to have a working gtk4 app
# This should just work on a Pinephone with bookworm

import gi
import importlib
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("GTK4 Beispiel")
    win.set_default_size(300, 200)
    btn = Gtk.Button(label="Measure distance")
    btn.connect('clicked', lambda x: measure_distance(btn)) # win.close())
    win.set_child(btn)
    win.present()

def measure_distance(self):

    # The submodule for the BOSCH devices.
    # Has to be done that way because of the "-" in the Name

    rangefinder = importlib.import_module("BOSCH-GLM-rangefinder.glm100c")
    print("rangefinder loaded in window as: " + str(rangefinder))

    try:
        print("Initializing GLM50C")
        glm50c = rangefinder.GLM50C()
        if not glm50c.connected:
            distance = "No Connection"
            self.set_label(distance)
        distance = glm50c.measure_from_tripod_socket(glm50c)
        if distance != -1:
            self.set_label(distance)
        else:
            distance = "No value measured"

    except OSError:
        print("No Device connected")
        distance = "OS error"
        self.set_label(distance)
    except ConnectionError:
        print("No Connection possible")
        distance = "Connection Error"
        self.set_label(distance)


app = Gtk.Application(application_id='org.petrisch.distance')
app.connect('activate', on_activate)
app.run(None)
