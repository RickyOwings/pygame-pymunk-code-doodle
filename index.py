import pygame, pymunk, pymunk.pygame_util, sys
from Player import Player
from MapTile import MapTile, initMap
from Camera import camera
from GameObject import GameObject, updateAllGO, drawAllGO, instances

print(len(sys.argv))

if len(sys.argv) == 3:
    RESOLUTION: tuple[float, float] = (float(sys.argv[1]), float(sys.argv[2]))
else:
    RESOLUTION: tuple[float, float] = (1920.0, 1080.0)
#CONSTANTS
FRAMERATE = 240.0


#setting up pygame
pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True

#setting up pymunk
space = pymunk.Space()
draw_options = pymunk.pygame_util.DrawOptions(screen)

space.gravity = (0, 1000)

#initialization of things in scene
player = Player(
    screen, 
    space, 
    (
        RESOLUTION[0]/2, 
        RESOLUTION[1]/2
    )
)
def cameraToPlayer():
    camera["dx"] = player.body.position[0] - RESOLUTION[0]/2
    camera["dy"] = player.body.position[1] - RESOLUTION[1]/2

initMap(screen, space)
print(f"There are {len(instances)} gameobject(s)!")


# --------------GAME LOOP--------------
while running:
    # ---CHECKING IF GAME IS TO CLOSE---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateAllGO(1000/FRAMERATE)
    cameraToPlayer()
    space.step(1.0/FRAMERATE)

    screen.fill(0x111111)

    drawAllGO()

    pygame.display.flip()
    clock.tick(FRAMERATE)

pygame.quit()