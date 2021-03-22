# -*- coding: utf-8 -*-

# Distance measuring tool

import subprocess
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
#print(sys.path)

#from distance import window
import src.window as window

#The submodule for the BOSCH devices
import importlib
rangefinder = importlib.import_module("BOSCH-GLM-rangefinder.glm100c")
#, package='BOSCH-GLM-rangefinder')

#When flatpak
#from distance import setup as setup

print("try setup")

#import pathlib
#print(pathlib.Path(__file__).parent.absolute())

#response = subprocess.run(['python3', 'setup.py', 'install'])
#response = subprocess.run(['/usr/bin/ls', '-l', '/home/petrisch'], capture_output=True, text=True)
#print(response.stdout)

print("made setup")

#When flatpak
#from distance import glm100c


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


if rangefinder == None:
    print("rangefinder not loaded")
else:
    print("rangefinder loaded as: " + str(rangefinder))

def main(version):
    print("Entering Window part now")
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
    print("I am called as main from the main module")
    main("0.1.0")
    
