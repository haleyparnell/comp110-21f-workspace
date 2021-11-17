import pygame
import math
from vector import Vector
class Ball:
    """Objects player is defending against."""
    position: Vector
    color: tuple
    speed: float = 5.0

    def __init__(self, position: Vector, color: tuple, speed: float):
        self.position = position
        self.color = color
        self.speed = speed

    def move_ball(self, new_position: Vector) -> None:
        self.x += self.velocity
        self.y += self.angle