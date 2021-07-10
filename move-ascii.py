import sys
import time
import simpleaudio as sa
from asciimatics.screen import Screen


# load sounds
stepping = sa.WaveObject.from_wave_file("step.wav")
bump = sa.WaveObject.from_wave_file("bump.wav")


def draw(screen: Screen, x: int, y: int, char: str):
    screen.print_at(char, x, y, colour=2)  # 2 for green
    screen.refresh()

def demo(screen):
    # height of the ground in pixels
    g = screen.height // 4
    # start in the middle, above ground
    x, y = screen.width // 2, screen.height - g - 1
    STEP = 1
    for i in range(1, screen.width - 1):
        draw(screen, i, screen.height - g, "-")
    # draw char start
    draw(screen, x, y, "@")
    while True:
        s = 0
        try:
            inp = screen.get_key()
        except KeyboardInterrupt:
            sys.exit(0)
            # This still throws an error on exit, not sure why
        if inp == Screen.KEY_RIGHT:
            s = STEP
        elif inp == Screen.KEY_LEFT:
            s = -STEP
        elif inp == ord("q"):
            sys.exit(0)
        if s != 0:
            # Erase where the character was
            draw(screen, x, y, " ")
            # Try to move
            x += s
            if not (0 < x < screen.width):
                x -= s
                bump.play()
            else:
                stepping.play()
        draw(screen, x, y, "@")


Screen.wrapper(demo)
