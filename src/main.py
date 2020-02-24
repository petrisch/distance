# -*- coding: utf-8 -*-

# Proximity example
# This file is part of the Librem 5 developer documentation.

# Copyright (C) 2020 Purism SPC
# SPDX-License-Identifier: GPL-3.0+
# Author: David Boddie <david.boddie@puri.sm>

import sys
import gi
from .sensor import Proximity

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='com.example.proximity')
        GLib.set_application_name(_('Proximity'))
        GLib.set_prgname('com.example.proximity')

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

        self.add(self.label)

    def update_info(self, sensor, near):

        if near:
            self.label.set_markup(
                _('<span size="large"><b>Near</b></span>'))
        else:
            self.label.set_markup(
                _('<span size="large">Far</span>'))


def main(version):

    app = Application()
    return app.run(sys.argv)
