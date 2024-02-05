import math
from tkinter import Canvas, Event


class Sand:
    GRAIN_SIZE = 10
    sand_grains: list[int] = []

    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        self.canvas = canvas
        self.width_pixels = width
        self.height_pixels = height
        self.width = width / self.GRAIN_SIZE
        canvas.bind("<Button-1>", self.add_grain)

    def add_grain(self, event: Event) -> None:
        x_index, y_index = self.get_grid_position(event.x, event.y)

        x = x_index * self.GRAIN_SIZE
        y = y_index * self.GRAIN_SIZE

        grain = self.canvas.create_rectangle(
            x, y, x + self.GRAIN_SIZE, y + self.GRAIN_SIZE, fill="orange"
        )

        self.sand_grains.append(grain)

    def update(self) -> None:
        ...

    def move_grain(self, grain: int, diff_x: int, diff_y: int) -> None:
        # TODO
        # self.canvas.move(grain, diff_x * self.GRAIN_SIZE, diff_y * self.GRAIN_SIZE)
        ...

    def get_grain_position(self, grain: int) -> tuple[int, int]:
        return self.get_grid_position(*self.canvas.coords(grain))

    def get_grid_position(self, x: float, y: float) -> tuple[int, int]:
        x_index = math.floor(x / self.GRAIN_SIZE)
        y_index = math.floor(y / self.GRAIN_SIZE)
        return x_index, y_index
