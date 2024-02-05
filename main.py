import time
import tkinter as tk


class App(tk.Tk):
    WINDOW_HEIGHT = 500
    WINDOW_WIDTH = 700
    REFRESH_RATE = 0.01

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

    def loop(self) -> None:
        while True:
            self.draw()
            self.update_idletasks()
            self.update()
            time.sleep(self.REFRESH_RATE)

    def draw(self) -> None:
        ...


if __name__ == "__main__":
    app = App()
    app.loop()
