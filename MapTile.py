import pygame, pymunk
from GameObject import GameObject
from Camera import camera

# -----TILE CONSTANTS-----
T_COLOR = 0x444444
T_SIZE = 100
T_POLY = [
    (-T_SIZE/2, -T_SIZE/2),
    (T_SIZE/2, -T_SIZE/2),
    (T_SIZE/2, T_SIZE/2),
    (-T_SIZE/2, T_SIZE/2),
]
T_RAMP = [
    (T_SIZE/2, 0),
    (T_SIZE/2, T_SIZE/2),
    (-T_SIZE/2, T_SIZE/2),
]

T_MASS = 100.0

MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,2,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
]
# -----TILE CONSTANTS-----







class MapTile(GameObject):


    def __init__(
            self, 
            surface: pygame.Surface,
            space: pymunk.Space,
            position: tuple[float, float] = (0,0),
            type: int = 1
            ):
        super().__init__()
        match(type):
            case 1:
                shape = T_POLY
            case 2:
                shape = T_RAMP
            case _:
                shape = T_POLY




        # drawing surface for pygame
        self.surface = surface
        # space for pymunk
        self.space = space

        # phsyics body
        self.body = pymunk.Body()
        self.body.body_type = pymunk.Body.STATIC
        self.body.position = position
        self.body.angle = 0

        self.index = len(space.bodies)
        # physics shape
        self.shape = pymunk.Poly(self.body, shape)
        self.shape.friction = 1
        self.space.add(self.body, self.shape)



    def draw(self):
        dCam = (camera["dx"], camera["dy"])
        l_verts = self.shape.get_vertices()
        w_verts = [self.body.position + v.rotated(self.body.angle) - dCam for v in l_verts]
        w_int = [(int(vert[0]), int(vert[1])) for vert in w_verts]
        pygame.draw.polygon(self.surface, T_COLOR, w_int)


def initMap(surface: pygame.Surface, space: pymunk.Space):
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if MAP[y][x]:
                MapTile(surface, space, (x * T_SIZE, y * T_SIZE), MAP[y][x])