# -*- coding: utf-8 -*-

# Add some doku

import sys
import gi
from .sensor import Proximity

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_idgi='com.petrisch.distance')
        GLib.set_application_name(_('Distance'))
        GLib.set_prgname('com.petrisch.distance')

    def do_activate(self):

        window = Window(application=self)
        window.set_default_size(320, 512)
        window.show_all()

        self.proximity = Proximity()
        self.proximity.connect('changed', window.update_info)
        self.proximity.claim()

    def do_shutdown(self):
        self.proximity.release()


class Window(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = Gtk.Label(halign='center')
        self.label.set_markup(
            _('<span size="large">Waiting for changes</span>'))

#By commenting this out, we no longer see the label for the proximity sensor.
#Maybe we will use this later. Then we would need some sort of Grid to put these on. But maybe we use a .ui file.
#        self.add(self.label)

        self.button = Gtk.Button(label="Measure")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.CENTER)

        self.add(self.button)


    def update_info(self, sensor, near):

        if near:
            self.label.set_markup(
                _('<span size="large"><b>Near</b></span>'))
        else:
            self.label.set_markup(
                _('<span size="large">Far</span>'))


#Thats how to connect the button
#         self.box = Gtk.Box(spacing=6)
#         self.add(self.box)

#         self.button = Gtk.Button(label="Click Here")
#         self.button.set_halign(Gtk.Align.CENTER)
#         self.button.set_valign(Gtk.Align.CENTER)
#         self.button.connect("clicked", self.on_button_clicked)
#         self.box.pack_start(self.button, True, True, 0)




def main(version):

    app = Application()
    return app.run(sys.argv)
