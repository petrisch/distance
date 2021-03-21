# -*- coding: utf-8 -*-

# The ui handling part

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
from gi_composites import GtkTemplate
#from __future__ import print_function

#The submodule for the BOSCH devices
import importlib
rangefinder = importlib.import_module("BOSCH-GLM-rangefinder.glm100c")

#class Application(Gtk.Application):

#    def __init__(self):
#        super().__init__(application_id='com.petrisch.distance')
#        GLib.set_application_name(_('Distance'))
#        GLib.set_prgname('com.petrisch.distance')

#    def do_activate(self):
#        builder = Gtk.Builder()
#        When using flatpak
#        builder.add_from_resource('/com/petrisch/distance/src/distance_window.ui')
#        window = builder.get_object("DistanceWindow")
#        window = Window(application=self)

#         window.set_default_size(320, 512)
#        window.show_all()

#        self.distance = Distance()
#        self.distance.connect('changed', window.update_info)
#        self.distance.claim()


#    def do_shutdown(self):
#        TODO: Shut down the connection when finished
#         self.distance.release()
#        return ""


@GtkTemplate(ui='src/distance_window.ui')
class DistanceWindow(Gtk.Box):

    __gtype_name__ = 'DistanceWindow'
    measure_button1 = GtkTemplate.Child()

    print("Trying init")

    def __init__(self):
        #super(Gtk.Box, self).__init__()
        print("Trying init 2")
        super().__init__()
        self.init_template()
        self.measure_button1.clicked()


    @GtkTemplate.Callback
    def measure_button1_clicked_cb(self, widget):
        distance = measure_distance(self)
        print("The distance is:" + distance)
        self.distance1_label.set_markup(
        _('<span size="large">Distance 1 is:' + distance + '</span>'))
        #def  measure_button = self.get_object("measure_button")
        #measure_button.connect("clicked", self.measure_button_clicked_cb)
        #distance1_label = self.get_object("distance1_label")


def measure_distance(self):
    print("Trying to measure distance")
    print("rangefinder loaded in window as: " + str(rangefinder))
    if not rangefinder.GLM.connected: exit(1)

    distance = rangefinder.measure_from_tripod_socket()
    if distance != -1: return distance

def debugmessage():
    print("Window module is loaded")


