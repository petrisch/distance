# -*- coding: utf-8 -*-

# Distance measuring tool

import subprocess
import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import GLib, Gtk


#TODO:Most of the comments here are for a generall purpose when using a more packaged version with Flatpak.
#from distance import window
#from distance import glm100c
import src.window as window

#TODO: Maybe start the python setup, but only if flatpak doesn't work.
#from distance import setup as setup
#import pathlib
#print(pathlib.Path(__file__).parent.absolute())
#response = subprocess.run(['python3', 'setup.py', 'install'])
#response = subprocess.run(['/usr/bin/ls', '-l', '/home/petrisch'], capture_output=True, text=True)
#print(response.stdout)

#Not used if flatpak with distance.in
import gettext
import locale
import os
import signal
import sys

VERSION = '@VERSION@'
pkgdatadir = '@pkgdatadir@'
localedir = '@localedir@'

sys.path.insert(1, pkgdatadir)
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Enable translation to occur in the extension libraries.
locale.bindtextdomain('@project_name@', localedir)
locale.textdomain('@project_name@')

# Install a translator for Python code to use throughout the application.
gettext.install('@project_name@', localedir, names=['ngettext'])


def main(version):
    print("Basic modules loaded")
    print("Entering GUI now")

    #app = window.Application()
    distancewin = window.DistanceWindow()

    win = Gtk.Window()
    win.connect('delete-event', Gtk.main_quit)

    #window = DistanceWindow()
    win.add(distancewin)
    win.show_all()
    return Gtk.main()
    #return app.run(sys.argv)

if __name__ == "__main__":

    version = "0.0.1"

    print("::::::::::::::::::::::::::")
    print("Welcome to distance " + version + ": The tool for measuring distances")
    print("::::::::::::::::::::::::::")

    main(version)
    
