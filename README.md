# deskswitch

DeskSwitch is a little app indicator that lets you switch the folder your desktop points to. This can be really useful in keeping the desktop area useful and organized by what your are doing at the time.

DeskSwitch expects a `dswitch.conf` file to be present in `$HOME/.config/` that specifies the folders it can swap to. There is a sample conf file in the repository.

###Installation Instructions

clone this repository in the `/opt/` folder, then `cd /opt/deskswitch/` and run `cp sample.conf ~/.config/dswitch.conf`

now, you can open the conf file with your favorite text editor and change it to your liking; try `gedit ~/.config/dswitch.conf`

to run the app indicator press Alt+F2 (on ubuntu) and type in `/opt/deskswitch/dswitch.py`

you can also set it to run at startup as you do any other application if you choose, simply set `/opt/deskswitch/dswitch.py` as the command to run