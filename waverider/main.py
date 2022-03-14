"""
Wave Rider -- A Python Adventure Through Soundscapes

    This is a game about a little glider dude going after some things and his path makes a wave. That wave becomes
    a sound wave. And that sound wave makes its way to your ears.

Author: Mike Fredricks
Genesis: 2/13/2022
"""
import sys
import logging
from Module import global_variables as gv

logger = logging.getLogger(__name__)

VERSION = '0.1'

try:
    import os
    import pygame as pg
except ImportError as error:
    # TODO: Add ImportError logging
    logger.warning('This is a warning')
    print(str(error) + ": failed to load module(s)")
except Exception as exception:
    # TODO: Add Exception logging
    sys.exit()


# Make sure these modules import properly
if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

# Initialize game directory
main_directory = os.path.split(os.path.abspath(__file__))[0]

# Main game execution function
def main():

    # Initialize pygame and create popout window
    pg.init()
    screen = pg.display.set_mode((1280, 720), pg.SCALED)
    screen.fill(gv.black)
    pg.display.set_caption("Wave Rider")
    pg.mouse.set_visible(False)

    # Create and set game clock
    clock = pg.time.Clock()
    clock_going = True

    # Main game loop
    while clock_going:
        clock.tick(60)

        # Track game event queue
        for event in pg.event.get():
            if event.type == pg.QUIT:
                clock_going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                clock_going = False

        # TODO: Draw everything onto screen

    # Pump out old events, and keep the queue current
    pg.event.pump()

    # Quit game
    pg.quit()

if __name__ == "__main__":
    main()



















