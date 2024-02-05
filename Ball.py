import math
import random
from tkinter import Canvas


class Ball:
    def __init__(
        self, canvas: Canvas, x: int, y: int, radius: int = 25, velocity: float = 1
    ) -> None:
        angle = 2 * math.pi * (random.random())
        self.dx = velocity * math.cos(angle)
        self.dy = velocity * math.sin(angle)
        self.canvas = canvas
        self.id = self.canvas.create_oval(
            x, y, x + 2 * radius, y + 2 * radius, fill="black"
        )

    def move(self, width: int, height: int) -> None:
        self.canvas.move(self.id, self.dx, self.dy)

        x0, y0, x1, y1 = self.canvas.coords(self.id)

        if x0 <= 0 or x1 >= width:
            self.dx = -self.dx

        if y0 <= 0 or y1 >= height:
            self.dy = -self.dy
