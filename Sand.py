import math
import random


class Sand:
    DEFAULT_GRAIN_SIZE = 10
    SAND_COLORS = ["#ffae00", "#ffb619", "#ffbc2b", "#ffc240"]
    _grains: list[list[str | None]]

    def __init__(
        self,
        width: int,
        height: int,
        grain_size: int = DEFAULT_GRAIN_SIZE,
    ) -> None:
        self._grain_size = grain_size
        self.width, self.height = self._get_grid_position(width, height)
        self._grains = [[None] * self.width for _ in range(self.height)]

    def add_grains(self, x: int, y: int) -> None:
        for r in range(0, self._grain_size * 5, self._grain_size):
            for deg in range(0, int(2 * math.pi * 2)):
                deg = deg / 2
                dx, dy = r * math.cos(deg), r * math.sin(deg)
                if random.random() < 0.5:
                    self.add_single_grain(int(x + dx), int(y + dy))

    def add_single_grain(self, x: int, y: int) -> None:
        grid_x, grid_y = self._get_grid_position(x, y)

        if self._can_move_to((grid_x, grid_y)):
            self._grains[grid_y][grid_x] = random.choice(self.SAND_COLORS)

    def update(self) -> None:
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width - 1, -1, -1):
                if self._grains[y][x] is None:
                    continue
                pos = x, y
                if self._can_move_to((target_pos := (x, y + 1))):
                    self._move_grain(pos, target_pos)
                elif self._can_move_to((target_pos := (x + 1, y + 1))):
                    self._move_grain(pos, target_pos)
                elif self._can_move_to((target_pos := (x - 1, y + 1))):
                    self._move_grain(pos, target_pos)

    def _can_move_to(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        return (
            0 <= y < self.height and 0 <= x < self.width and self._grains[y][x] is None
        )

    def _move_grain(self, pos: tuple[int, int], target_pos: tuple[int, int]) -> None:
        self._grains[target_pos[1]][target_pos[0]] = self._grains[pos[1]][pos[0]]
        self._grains[pos[1]][pos[0]] = None

    def _get_grid_position(self, x: int, y: int) -> tuple[int, int]:
        return (
            math.floor(x / self._grain_size),
            math.floor(y / self._grain_size),
        )

    def _get_real_position(self, grid_x: int, grid_y: int) -> tuple[int, int]:
        return grid_x * self._grain_size, grid_y * self._grain_size

    @property
    def grains_list(self) -> list[tuple[int, int, str]]:
        return [
            (x, y, color)
            for x in range(self.width)
            for y in range(self.height)
            if (color := self._grains[y][x])
        ]

    @property
    def grain_size(self) -> int:
        return self._grain_size
