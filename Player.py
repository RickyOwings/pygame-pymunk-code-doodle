import pygame, pymunk, math
from GameObject import GameObject
from Camera import camera

# -----PLAYER CONSTANTS-----
P_COLOR = 0x00FF00
P_SIZE = 40
P_POLY = [
    (-P_SIZE/2, -P_SIZE/2),
    (P_SIZE/2, -P_SIZE/2),
    (P_SIZE/2, P_SIZE/2),
    (-P_SIZE/2, P_SIZE/2),
]

P_MASS = 1.0
P_COLLISION_TYPE = 1

# -----PLAYER CONSTANTS-----







class Player(GameObject):


    def __init__(
            self, 
            surface: pygame.Surface,
            space: pymunk.Space,
            position: tuple[float, float] = (0,0),
            angle: float = 0
            ):
        super().__init__()
        # drawing surface for pygame
        self.surface = surface
        # space for pymunk
        self.space = space

        # phsyics body
        self.body = pymunk.Body()
        self.body.moment = pymunk.moment_for_box(P_MASS, (P_SIZE, P_SIZE))
        self.body.mass = P_MASS
        self.body.position = position
        self.body.angle = angle

        self.index = len(space.bodies)
        # physics shape
        self.shape = pymunk.Circle(self.body, P_SIZE/2)
        # self.shape = pymunk.Poly(self.body, P_POLY)
        self.shape.collision_type = P_COLLISION_TYPE
        self.shape.friction = 1
        self.space.add(self.body, self.shape)


    def update(self, time: float):
        super().update(time)
        keys = pygame.key.get_pressed()
        # presssing w and collding with something
        if keys[pygame.K_w]:
            self.body.apply_force_at_world_point((0,-1500), self.body.position)


        if keys[pygame.K_a]:
            self.body.apply_impulse_at_local_point((0,P_SIZE), (-1,0))
            self.body.apply_impulse_at_local_point((0,-P_SIZE), (1,0))

        if keys[pygame.K_d]:
            self.body.apply_impulse_at_local_point((0,P_SIZE), (1,0))
            self.body.apply_impulse_at_local_point((0,-P_SIZE), (-1,0))


    def draw(self):
        # l_verts = self.shape.get_vertices()
        # w_verts = [self.body.position + v.rotated(self.body.angle) for v in l_verts]
        # w_int = [(int(vert[0]), int(vert[1])) for vert in w_verts]
        # pygame.draw.polygon(self.surface, P_COLOR, w_int)
        dCam = (camera["dx"], camera["dy"])
        pygame.draw.circle(self.surface, P_COLOR, self.body.position - dCam, P_SIZE/2)
        pygame.draw.line(
            self.surface, 
            0x000000,
            pymunk.Vec2d(-P_SIZE/2, 0).rotated(self.body.angle) + self.body.position - dCam,
            pymunk.Vec2d(P_SIZE/2, 0).rotated(self.body.angle) + self.body.position - dCam
        )


