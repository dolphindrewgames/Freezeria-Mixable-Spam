# Freezeria Mixable Spam
A script to rapidly pour mixables in the Flash version of Papa's Freezeria.

## Requirements
- [Python 3.12](https://www.python.org/downloads/)
- [PyGetWindow](https://pypi.org/project/PyGetWindow/) and [pynput](https://pypi.org/project/pynput/) packages
    - `pip install pygetwindow pynput`
- [Flash Player Projector](https://archive.org/details/standaloneflashplayers) or [Ruffle Emulator](https://ruffle.rs/downloads)
- [Papa's Freezeria SWF](https://flipline.com/freegames.html)

## Instructions
- Launch the Flash Player Projector or Ruffle Emulator.
- Open the Papa's Freezeria SWF and start a day.
    - Do not resize the window once the game has loaded!
- Go to the Build Station, and reach the mixable screen.
- **Optional**: update the values in config.toml.
- Run the script:
    - `python freezeria_mixable_spam.py`