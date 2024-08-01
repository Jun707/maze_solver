from window import Window
from graph import Point, Line 
def main():
    win = Window(800, 600)
    point1 = Point(0, 300)
    point2 = Point(800, 300)
    line = Line(point1, point2)
    win.draw_line(line, "blue")
    win.wait_for_close()


main()