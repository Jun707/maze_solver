from tkinter import Tk, BOTH, Canvas
from graph import Line

class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Runner")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False