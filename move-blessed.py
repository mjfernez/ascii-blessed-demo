import sys
import time
from math import floor
from blessed import Terminal
import simpleaudio as sa

term = Terminal()
# load sounds
stepping = sa.WaveObject.from_wave_file("step.wav")
bump = sa.WaveObject.from_wave_file("bump.wav")


def close():
    """
    Closes the terminal and clears the screen
    """
    print(term.clear)
    sys.exit(0)


def draw(x: int, y: int, char: str):
    print(term.move_xy(x, y) + char, end="", flush=True)


with term.cbreak(), term.hidden_cursor():
    # clear the screen
    print(term.home + term.green_on_black + term.clear)
    # height of the ground in pixels
    g = term.height // 4
    # start in the middle, above ground
    x, y = term.width // 2, term.height - g - 1
    STEP = 1
    for i in range(1, term.width - 1):
        draw(i, term.height - g, "-")
    # draw char start
    draw(x, y, "@")
    while True:
        s = 0
        try:
            inp = repr(term.inkey())
        except KeyboardInterrupt:
            close()
        if inp == "KEY_RIGHT":
            s = STEP
        elif inp == "KEY_LEFT":
            s = -STEP
        # Apparently, letter keys are quoted in blessed
        elif inp == "'q'":
            close()
        if s != 0:
            # Erase where the character was
            draw(x, y, " ")

            # Try to move
            x += s
            if not (0 < x < term.width):
                x -= s
                bump.play()
            else:
                stepping.play()
        draw(x, y, "@")
