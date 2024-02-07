import tkinter as tk

from Sand import Sand


class App(tk.Tk):
    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1000
    REFRESH_RATE = 0.01

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")

        self.canvas = self.create_canvas()
        self.sand = Sand(self.canvas, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

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
            self.sand.update()
            self.update_idletasks()
            self.update()


if __name__ == "__main__":
    app = App()
    app.loop()
