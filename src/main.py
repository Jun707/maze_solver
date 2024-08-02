from window import Window
from graph import Point, Line, Cell
def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(20, 20, 100, 100)
    win.wait_for_close()

main()