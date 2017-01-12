#!/usr/bin/env python3

#----------------------------------------------------------------------------
#    "THE BEER-WARE LICENSE":
#    <imbuedhope@gmail.com> wrote this file.  As long as you retain this notice you
#    can do whatever you want with this stuff. If we meet some day, and you think
#    this stuff is worth it, you can buy me a beer in return.
# ----------------------------------------------------------------------------

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Nautilus', '3.0')

# imports
import os
import subprocess
from gi.repository import Gtk
from gi.repository import AppIndicator3 as aind

# switch desktops
def switch_to(w, buf):
    subprocess.call(["xdg-user-dirs-update", "--set", "DESKTOP", os.path.expanduser(buf)])
    subprocess.call(["killall", "nautilus"])
    subprocess.Popen(["nautilus", "--no-default-window"])

def quit(w, buf):
    exit(buf)
    

if __name__ == "__main__":
    ind = aind.Indicator.new("Desktop Switcher", "system", aind.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status(aind.IndicatorStatus.ACTIVE)
    ind.set_attention_icon("indicator-messages-new")

    # create a menu
    menu = Gtk.Menu()

    # create sub menus
    with open(os.path.expanduser("~/.config/dswitch.conf")) as config:
        for line in config:
            line = line.strip().split('#', 1)[0].strip()
            if line is not "":
                info = line.split()
                if (len(info) == 2) and os.path.isdir(os.path.expanduser(info[1])):
                    # create the menu!
                    menu_item = Gtk.MenuItem(info[0])
                    menu.append(menu_item)
                    menu_item.connect("activate", switch_to, info[1])
                    menu_item.show()


    # add a quit option to the app
    split = Gtk.SeparatorMenuItem().new()
    menu.append(split)
    split.show()

    quit_menu_item = Gtk.MenuItem("Quit")
    menu.append(quit_menu_item)
    quit_menu_item.connect("activate", quit, 0)
    quit_menu_item.show()

    ind.set_menu(menu)
    
    Gtk.main()
