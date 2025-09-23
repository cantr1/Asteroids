import pygame
import sys
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE
)

def main():
    try:
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            pygame.display.flip()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected, exiting gracefully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
