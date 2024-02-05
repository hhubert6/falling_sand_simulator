import random
import time
import tkinter as tk

from Ball import Ball


class App(tk.Tk):
    WINDOW_HEIGHT = 500
    WINDOW_WIDTH = 700
    REFRESH_RATE = 0.01

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.canvas = self.create_canvas()
        self.balls = [self.create_ball() for _ in range(10)]

    def create_ball(self) -> Ball:
        radius = 25
        return Ball(
            self.canvas,
            x=random.randint(0, self.WINDOW_WIDTH - 2*radius),
            y=random.randint(0, self.WINDOW_HEIGHT - 2*radius),
            radius=radius,
            velocity=random.randint(5, 10) / 2,
        )

    def create_canvas(self) -> tk.Canvas:
        canvas = tk.Canvas(
            self,
            bg="white",
            width=self.WINDOW_WIDTH,
            height=self.WINDOW_HEIGHT,
        )
        canvas.pack()
        return canvas

    def loop(self) -> None:
        while True:
            self.draw()
            self.update_idletasks()
            self.update()
            time.sleep(self.REFRESH_RATE)

    def draw(self) -> None:
        for ball in self.balls:
            ball.move(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)


if __name__ == "__main__":
    app = App()
    app.loop()
