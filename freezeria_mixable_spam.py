import pygetwindow as gw
from pynput.mouse import Button, Controller
import time
import tomllib
import random

# scaled X positions of the mixables (percentage of the window's width)
MIXABLE_SCALES_X = [
    0.09634146341463415,
    0.1975609756097561,
    0.5585365853658537,
    0.6609756097560976,
]

# scaled Y positions of the mixables (percentage of the window's height)
MIXABLE_SCALES_Y = [
    0.28197226502311246,
    0.4052388289676425,
]

# scaled X and Y positions of the pour button
POUR_SCALE_X = 0.375609756097561
POUR_SCALE_Y = 0.3220338983050847

# names of mixables
MIXABLE_NAMES = [
    "Nutty Butter Cups",
    "Strawberries",
    "Pineapple",
    "Blueberries",
    "Marshmallows",
    "Yum n' Ms",
    "Creameo Bits",
    "Cookie Dough",
]

def get_position(window, scale_x, scale_y):
    return {
        'x': scale_x * window.size.width + window.topleft.x,
        'y': scale_y * window.size.height + window.topleft.y,
    }

def get_mixable_positions(window):
    return [get_position(window, scale_x, scale_y) for scale_y in MIXABLE_SCALES_Y for scale_x in MIXABLE_SCALES_X]

def click(mouse, x, y, delay):
    mouse.position = (x, y)
    time.sleep(delay)
    mouse.click(Button.left)
    time.sleep(delay)

if __name__ == '__main__':
    with open('config.toml', 'rb') as f:
        config = tomllib.load(f)

    for title in config['WINDOW_TITLES']:
        windows = gw.getWindowsWithTitle(title)
        if windows: break
    else:
        raise Exception('Could not find a flash player.')

    window = windows[0]
    window.restore()
    window.activate()
    time.sleep(1)

    all_positions = get_mixable_positions(window)
    positions = [all_positions[i] for i, mixable in enumerate(MIXABLE_NAMES) if config['ALLOW_MIXABLES'][mixable]]
    pour_button = get_position(window, POUR_SCALE_X, POUR_SCALE_Y)

    mouse = Controller()
    for _ in range(config['NUM_MIXABLES']):
        position = positions[random.randint(0, len(positions) - 1)]
        click(mouse, position['x'], position['y'], config['CLICK_DELAY'])
        click(mouse, pour_button['x'], pour_button['y'], config['CLICK_DELAY'])