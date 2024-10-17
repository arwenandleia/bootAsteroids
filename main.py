import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main ():
    pygame.init()
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt=0
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group,drawable_group)
    Asteroid.containers = (asteroids_group,updatable_group,drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group,updatable_group,drawable_group)

    my_player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    my_asteroid_field = AsteroidField()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        for updatable in updatable_group:
            updatable.update(dt)

        for asteroid in asteroids_group:
            if my_player.is_collision(asteroid):
                print('Game Over!')
                exit()
            
            for each_shot in shots_group:
                if each_shot.is_collision(asteroid):
                    each_shot.kill()
                    asteroid.split()
        


        
        for drawable in drawable_group:
            drawable.draw(screen)

        
        pygame.display.flip()
        dt = game_clock.tick(60)/1000.0


    

if __name__ == '__main__':
    main()
