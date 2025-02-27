import sys
import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    game_state = "start_menu"



    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    asteroid_field = AsteroidField()

     # Menus
    def draw_start_menu():
        font = pygame.font.SysFont("arial", 40)
        title = font.render("Asteroids", True, (255,255,255))
        sub_title = font.render("Press ""ENTER"" to start", True, (255,255,255))
        screen.blit(title, (x - title.get_width()/2, y - title.get_height()/2))
        screen.blit(sub_title, (x - sub_title.get_width()/2, y + sub_title.get_height()/2))
        pygame.display.update()
    
    def draw_game_over_menu():
        font = pygame.font.SysFont("arial", 40)
        title = font.render("GAME OVER", True, (255,255,255))
        sub_title = font.render("Press ""ENTER"" to try again", True, (255,255,255))
        screen.blit(title, (x - title.get_width()/2, y - title.get_height()/2))
        screen.blit(sub_title, (x - sub_title.get_width()/2, y + sub_title.get_height()/2))
        pygame.display.update()

    # Game loop
    while True:
        
        #Makes it possible to close screen using the "X" button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Update game
        updatable.update(dt)
        screen.fill("black")
        keys = pygame.key.get_pressed()


        if keys[pygame.K_KP_ENTER] and game_state == "start_menu":
                game_state = "game_start"

        if keys[pygame.K_KP_ENTER] and game_state == "game_over":
                game_state = "game_start"
                main()
                

        if game_state == "start_menu":
            draw_start_menu()
        elif game_state == "game_over":
            draw_game_over_menu()

        if game_state == "game_start":
            # check for astroid collision with player
            for astroid in asteroids:
                if astroid.collision(player):
                    # If collision with player draw "Game Over" screen
                    game_state = "game_over"

            # check for astroid collision with shot
            for astroid in asteroids:
                for shot in shots:
                    if astroid.collision(shot):
                        shot.kill()
                        astroid.split()


            for obj in drawable:
                obj.draw(screen)



        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()


