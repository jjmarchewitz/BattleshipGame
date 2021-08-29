""" game.py

The main game script.

GitHub: https://github.com/jjmarchewitz/BattleshipGame
PyGame Docs: https://www.pygame.org/docs/
"""

import pygame as pg
from dataclasses import dataclass, field


@dataclass
class GameProperties:
    running: bool = True
    window_width: int = 500
    window_height: int = 500
    background_color: str = "#0ABBFF"


properties = GameProperties()


def main():
    """Entry-point into the program."""
    # Initialize pygame
    pg.init()

    # Verify that pygame initialized correctly
    if not pg.display.get_init():
        raise SystemError("Display module did not properly initialize.")

    # Open a new window at the desired dimensions and set its properties
    display_surface = pg.display.set_mode(
        (properties.window_width, properties.window_height)
    )
    pg.display.set_caption("Battleship")

    # Main display loop
    while properties.running:
        process_pygame_events()
        pg.display.flip()
        draw_window(display_surface)

    # Quit pygame
    pg.quit()


def process_pygame_events():
    """Process all of the pygame events pulled from pg.event.get()."""
    # Process pygame events
    for event in pg.event.get():
        # Quit condition
        if event.type is pg.QUIT:
            properties.running = False


def draw_window(surface):
    surface.fill(properties.background_color)


# Guard to prevent this script from being executed when imported. "__name__" won't equal
# "__main__" unless this script is run from the command line to protect it from running.
if __name__ == "__main__":
    main()
