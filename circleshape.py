import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_collision(self,other_object):
        first_position = self.position
        first_radius = self.radius
        second_position = other_object.position
        second_radius = other_object.radius

        distance_between_objects = first_position.distance_to(second_position)
        if distance_between_objects > first_radius + second_radius:
            return False
        else:
            return True
    



