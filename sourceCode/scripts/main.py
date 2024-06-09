
"""
NOTE: the semicolons ';' have been used in the program as out of habbit and it will work without a doubt
with or without them. They are used for consistency.

The comments have made respectively where a need is felt for elaboration.
    - Book followed : "Making Games with python and Pygame by AI Sweigart"
    - Assets : https://pixelfrog-assets.itch.io/tiny-swords
    - Devlopers : 
                - https://github.com/124k3
                - https://github.com/Digital-Pirate 
"""

import pygame, sys;
from pygame.locals import *;


class Game:

    def __init__(self, screenWidth: int, screenHeight: int, GAME_TITLE: str) -> None:
        pygame.init();

        self.DISPLAY_SURFACE = pygame.display.set_mode((screenWidth, screenHeight)); 
        pygame.display.set_caption(GAME_TITLE); 
        self.fpsClock = pygame.time.Clock(); 


    def handleEvents(self) -> None:
        for event in pygame.event.get():
            # quitting the game on closing the app or pressing ESC
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit(); 
                sys.exit(); 

    def update(self) -> None:
        pygame.display.update();

    def render(self) -> None:
        pass

    def run(self, fps: int) -> None:

        while True:
            self.update()
            self.handleEvents();
            self.fpsClock.tick(fps); 



if __name__ == "__main__":

    screenHeight = 640;
    screenWidth = 1280;
    GameTitle = "2d Tekken"; 

    game = Game(screenWidth, screenHeight, GameTitle);
    fps = 30;
    game.run(fps);


