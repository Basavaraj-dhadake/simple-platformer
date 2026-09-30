import pygame

MAX_FALL_SPEED = 20  # terminal velocity (pixels/frame)


class Player:
    def __init__(self, x, y, width=24, height=32):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.speed = 4
        self.jump_strength = -12
        self.on_ground = False

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def jump(self):
        """Returns True if a jump actually happened."""
        if self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False
            return True
        return False
