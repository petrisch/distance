# Copyright (C) 2020 Purism SPC
# SPDX-License-Identifier: GPL-3.0+
# Author: David Boddie <david.boddie@puri.sm>

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, GObject


class Proximity(GObject.GObject):

    __gsignals__ = {
        'changed': (GObject.SIGNAL_RUN_FIRST, None, (bool,))
    }

    def __init__(self):
        GObject.GObject.__init__(self)

        # Request a proxy for accessing the sensor service.
        self.proxy = Gio.DBusProxy.new_for_bus_sync(
            Gio.BusType.SYSTEM, Gio.DBusProxyFlags.NONE, None,
            'net.hadess.SensorProxy',
            '/net/hadess/SensorProxy',
            'net.hadess.SensorProxy',
            None)

        # Track D-Bus property changes.
        self.proxy.connect('g-properties-changed',
                           self.properties_changed, None)

    def properties_changed(self, proxy, changed, invalidated, user_data):

        print(changed, invalidated)
        near = proxy.get_cached_property('ProximityNear').get_boolean()
        self.emit('changed', near)

    def claim(self):

        if self.proxy.get_cached_property('HasProximity').get_boolean():
            self.proxy.call_sync('ClaimProximity', None, Gio.DBusCallFlags.NONE,
                                 -1, None)

    def release(self):

        if self.proxy.get_cached_property('HasProximity').get_boolean():
            self.proxy.call_sync('ReleaseProximity', None, Gio.DBusCallFlags.NONE,
                                 -1, None)
