import pygame as pg

from Sand import Sand

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def draw_sand(screen: pg.Surface, sand: Sand) -> None:
    for x, y, color in sand.grains_list:
        rect = pg.Rect(
            (x * sand.grain_size, y * sand.grain_size), (sand.grain_size,) * 2
        )
        pg.draw.rect(screen, color, rect)


def handle_add_sand(sand: Sand) -> None:
    mouse_pressed, _, _ = pg.mouse.get_pressed()
    if mouse_pressed:
        sand.add_grains(*pg.mouse.get_pos())


def main() -> None:
    # pg setup
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    running = True

    sand = Sand(SCREEN_WIDTH, SCREEN_HEIGHT)

    # main loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("white")

        sand.update()
        handle_add_sand(sand)
        draw_sand(screen, sand)

        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
