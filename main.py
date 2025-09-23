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
        # Print some variables
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        # Initialize Pygame
        pygame.init()

        # Setup clock
        clock = pygame.time.Clock()
        dt = 0
    

        # Create a screen
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Infinite while-loop to persist the screen
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            pygame.display.flip()
            delta = clock.tick(60)
            dt = delta / 1000

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected, exiting gracefully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
