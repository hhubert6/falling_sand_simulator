import math
from tkinter import Canvas, Event


class Sand:
    GRAIN_SIZE = 10
    grains: dict[tuple[int, int], int] = {}

    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        self.canvas = canvas
        self.width, self.height = self.get_grid_position(width, height)
        canvas.bind("<Button-1>", self.add_grain)

    def add_grain(self, event: Event) -> None:
        grid_x, grid_y = self.get_grid_position(event.x, event.y)

        x = grid_x * self.GRAIN_SIZE
        y = grid_y * self.GRAIN_SIZE

        grain = self.canvas.create_rectangle(
            x,
            y,
            x + self.GRAIN_SIZE,
            y + self.GRAIN_SIZE,
            fill="orange",
            outline="orange",
        )

        self.grains[grid_x, grid_y] = grain

    def update(self) -> None:
        should_move = []

        for x, y in self.grains:
            if self.can_move_to(x, y + 1):
                should_move.append((x, y, 0, 1))
            elif self.can_move_to(x + 1, y + 1):
                should_move.append((x, y, 1, 1))
            elif self.can_move_to(x - 1, y + 1):
                should_move.append((x, y, -1, 1))

        self.resolve_movement(should_move)

    def can_move_to(self, x, y):
        return (
            (x, y) not in self.grains and 0 <= x < self.width and 0 <= y < self.height
        )

    def resolve_movement(self, should_move: list[tuple[int, int, int, int]]) -> None:
        for x, y, dx, dy in should_move:
            if (x + dx, y + dy) not in self.grains:
                self.move_grain(x, y, dx, dy)

    def move_grain(self, x: int, y: int, dx: int, dy: int) -> None:
        target_x, target_y = x + dx, y + dy

        grain = self.grains[(x, y)]
        self.grains[(target_x, target_y)] = grain
        del self.grains[(x, y)]

        self.canvas.move(grain, dx * self.GRAIN_SIZE, dy * self.GRAIN_SIZE)

    def get_grain_position(self, grain: int) -> tuple[int, int]:
        return self.get_grid_position(*self.canvas.coords(grain))

    def get_grid_position(self, x: float, y: float) -> tuple[int, int]:
        return (
            math.floor(x / self.GRAIN_SIZE),
            math.floor(y / self.GRAIN_SIZE),
        )
