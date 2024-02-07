import math
import random


class Sand:
    DEFAULT_GRAIN_SIZE = 10
    SAND_COLORS = ["#ffae00", "#ffb619", "#ffbc2b", "#ffc240"]
    _grains: dict[tuple[int, int], str] = {}

    def __init__(
        self,
        width: int,
        height: int,
        grain_size: int = DEFAULT_GRAIN_SIZE,
    ) -> None:
        self._grain_size = grain_size
        self.width, self.height = self._get_grid_position(width, height)

    def add_grains(self, x: int, y: int) -> None:
        for r in range(0, self._grain_size * 3, self._grain_size):
            for deg in range(0, int(2 * math.pi * 2)):
                deg = deg / 2
                dx, dy = r * math.cos(deg), r * math.sin(deg)
                if random.random() < 0.5:
                    self.add_single_grain(int(x + dx), int(y + dy))

    def add_single_grain(self, x: int, y: int) -> None:
        grid_x, grid_y = self._get_grid_position(x, y)

        if (grid_x, grid_y) not in self._grains:
            self._grains[grid_x, grid_y] = random.choice(self.SAND_COLORS)

    def update(self) -> None:
        coords = sorted(self._grains.keys(), key=lambda p: p[::-1], reverse=True)

        for pos in coords:
            x, y = pos
            if self._can_move_to(*(target_pos := (x, y + 1))):
                self._move_grain(pos, target_pos)
            elif self._can_move_to(*(target_pos := (x + 1, y + 1))):
                self._move_grain(pos, target_pos)
            elif self._can_move_to(*(target_pos := (x - 1, y + 1))):
                self._move_grain(pos, target_pos)

    def _can_move_to(self, x: int, y: int) -> bool:
        return (
            (x, y) not in self._grains and 0 <= x < self.width and 0 <= y < self.height
        )

    def _move_grain(self, pos: tuple[int, int], target_pos: tuple[int, int]) -> None:
        self._grains[target_pos] = self._grains.pop(pos)

    def _get_grid_position(self, x: int, y: int) -> tuple[int, int]:
        return (
            math.floor(x / self._grain_size),
            math.floor(y / self._grain_size),
        )

    def _get_real_position(self, grid_x: int, grid_y: int) -> tuple[int, int]:
        return grid_x * self._grain_size, grid_y * self._grain_size

    @property
    def grains_list(self) -> list[tuple[int, int, str]]:
        return [(*pos, color) for pos, color in self._grains.items()]

    @property
    def grain_size(self) -> int:
        return self._grain_size
