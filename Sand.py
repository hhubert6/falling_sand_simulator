import math
import random
from tkinter import Canvas, Event


class Sand:
    GRAIN_SIZE = 10
    grains: dict[tuple[int, int], int] = {}

    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        self.canvas = canvas
        self.width, self.height = self.get_grid_position(width, height)

        canvas.bind("<Button-1>", self.add_grains)
        canvas.bind("<B1-Motion>", self.add_grains)

    def add_grains(self, event: Event) -> None:
        for r in range(0, self.GRAIN_SIZE * 4, self.GRAIN_SIZE):
            for deg10 in range(0, int(2 * math.pi * 5)):
                deg = deg10 / 5
                dx, dy = r * math.cos(deg), r * math.sin(deg)
                if random.random() < 0.5:
                    self.add_single_grain(event.x + dx, event.y + dy)

    def add_single_grain(self, x: float, y: float) -> None:
        grid_x, grid_y = self.get_grid_position(x, y)

        if (grid_x, grid_y) in self.grains:
            return

        x = grid_x * self.GRAIN_SIZE
        y = grid_y * self.GRAIN_SIZE

        color = random.choice(["#ffae00", "#ffb619", "#ffbc2b", "#ffc240"])
        grain = self.canvas.create_rectangle(
            x,
            y,
            x + self.GRAIN_SIZE,
            y + self.GRAIN_SIZE,
            fill=color,
            outline=color,
        )

        self.grains[grid_x, grid_y] = grain

    def update(self) -> None:
        coords = sorted(self.grains.keys(), key=lambda p: p[::-1], reverse=True)

        for x, y in coords:
            if self.can_move_to(x, y + 1):
                self.move_grain(x, y, 0, 1)
            elif self.can_move_to(x + 1, y + 1):
                self.move_grain(x, y, 1, 1)
            elif self.can_move_to(x - 1, y + 1):
                self.move_grain(x, y, -1, 1)

    def can_move_to(self, x, y):
        return (
            (x, y) not in self.grains and 0 <= x < self.width and 0 <= y < self.height
        )

    def move_grain(self, x: int, y: int, dx: int, dy: int) -> None:
        target_x, target_y = x + dx, y + dy

        grain = self.grains.pop((x, y))
        self.grains[target_x, target_y] = grain

        self.canvas.move(grain, dx * self.GRAIN_SIZE, dy * self.GRAIN_SIZE)

    def get_grain_position(self, grain: int) -> tuple[int, int]:
        return self.get_grid_position(*self.canvas.coords(grain))

    def get_grid_position(self, x: float, y: float) -> tuple[int, int]:
        return (
            math.floor(x / self.GRAIN_SIZE),
            math.floor(y / self.GRAIN_SIZE),
        )
