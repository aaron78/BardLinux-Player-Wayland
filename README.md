# BardLinux-Player (Wayland)

Python script that plays MIDI files in Final Fantasy XIV's Bard Performance Mode, akin to BardMusicPlayer, but for Linux!

This version exists because the original project uses a graphical library that requires an X server. I've modified the keyboard input to use the [ydotool](https://github.com/ReimuNotMoe/ydotool) utility, which is compatible with Wayland. This utility creates a virtual input device when the daemon, ydotoold, runs. The command line utility, ydotool, can then pass commands to the daemon having it simulate input from the virtual device . You'll need to install and setup ydotool to use this project. I've also removed the GUI completely in favor of selecting files from the command line.

#### To install dependencies:

Install ydotool, most distributions probably have it in the repositories already. If no you can obtain the source from the projects github page [here](https://github.com/ReimuNotMoe/ydotool).

Example installing on Arch Linux:
`sudo pacman -S ydotool`

You'll need to have the systemd user service running to setup the virtual input device. You can set the service to automatically start up when you login and also start it now with:
`systemctl --user enable --now ydotool`

You'll need to also install the python library dependencies. I recommend you use a virtual environment, you can get details on that [here](https://docs.python.org/3/library/venv.html).
`pip install -r requirements.txt`

#### Before running:

Ensure keybindings are set as per ![BardMusicPlayer's settings](https://github.com/aaron78/BardLinux-Player-Wayland/blob/main/perf_settings.png)

#### Running:

- Open up Bard Performance Mode in FFXIV with instrument of choice

- Run `./play.py <FILE>`. The File argument can be a relative or full path.

- Switch back to FFXIV, and rock out

Playing will start after a 3 second delay. This can be updated in play.py, under the sleep(3) function.
