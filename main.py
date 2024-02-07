import pygame as pg

from Sand import Sand

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def draw_sand(screen: pg.Surface, sand: Sand) -> None:
    for pos, color in sand.get_grains():
        rect = pg.Rect(pos, (sand.get_grain_size(), sand.get_grain_size()))
        pg.draw.rect(screen, color, rect)


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

        mouse_pressed, _, _ = pg.mouse.get_pressed()
        if mouse_pressed:
            sand.add_grains(*pg.mouse.get_pos())

        draw_sand(screen, sand)

        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
