""" game.py

The main game script.

GitHub: https://github.com/jjmarchewitz/BattleshipGame
PyGame Docs: https://www.pygame.org/docs/
"""

import pygame as pg
import time
from dataclasses import dataclass


@dataclass
class States:
    paused: str = "PAUSED"
    normal_speed: str = "NORMAL_SPEED"
    fast_forward: str = "FAST_FORWARD"


@dataclass
class GameProperties:
    state: str
    running: bool = True
    window_width: int = 500
    window_height: int = 500
    sleep_time: int = 500
    background_color: str = "#0ABBFF"
    grid_color: str = "#303030"


class BotRunner:
    def __init__(self):
        self.states = States()
        self.properties = GameProperties(self.states.paused)
        self.buttons = {
            "PLAY/PAUSE": None,
        }

        self.run()

    def run(self):
        """Entry-point into the program."""
        # Initialize pygame
        pg.init()

        # Verify that pygame initialized correctly
        if not pg.display.get_init():
            raise SystemError("Display module did not properly initialize.")

        # Open a new window at the desired dimensions and set its properties
        display_surface = pg.display.set_mode(
            (self.properties.window_width, self.properties.window_height)
        )
        pg.display.set_caption("Battleship")
        window_icon = pg.image.load("Assets/window_icon.png")
        pg.display.set_icon(window_icon)

        # Main display loop
        while self.properties.running:
            self.process_pygame_events()

            # Paused state
            if self.properties.state == self.states.paused:
                self.paused(display_surface)
            # Normal speed
            elif self.properties.state == self.states.normal_speed:
                self.simulation_running_normal(display_surface)
            # Fast-forward
            elif self.properties.state == self.states.fast_forward:
                self.simulation_running_ff(display_surface)

            else:
                raise Exception("Invalid state.")

            pg.display.flip()

        # Quit pygame
        pg.quit()

    ##############
    # STRUCTURAL #
    ##############

    def process_pygame_events(self):
        """Process all of the pygame events pulled from pg.event.get()."""
        # Process pygame events
        for event in pg.event.get():
            # Quit condition
            if event.type is pg.QUIT:
                self.quit_program()

    def quit_program(self):
        """Exit the program."""
        self.properties.running = False

    def process_game_buttons(self):
        """Process any button events pn the main menu."""
        pass

    ##########
    # PAUSED #
    ##########

    def paused(self, surface):
        """High-level pause screen."""
        self.process_game_buttons()
        self.draw_paused_screen(surface)

    def draw_paused_screen(self, surface):
        """Draw the main menu on the display surface."""
        surface.fill(self.properties.background_color)

    ################
    # GAME RUNNING #
    ################

    def simulation_running_normal(self, surface):
        """High-level running simulation at normal speed."""
        self.process_game_buttons()
        self.draw_running_simulation(surface)
        time.sleep(self.properties.sleep_time)

    def simulation_running_ff(self, surface):
        """High-level running simulation at unrestricted speed."""
        self.process_game_buttons()
        self.draw_running_simulation(surface)

    def draw_running_simulation(self, surface):
        """Draw one iteration of the running game."""
        self.process_game_buttons()
        surface.fill(self.properties.background_color)


# Guard to prevent this script from being executed when imported. "__name__" won't equal
# "__main__" unless this script is run from the command line to protect it from running.
if __name__ == "__main__":
    game = BotRunner()
