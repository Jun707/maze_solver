from tkinter import Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill= fill_color, width=2
        )

class Cell:

    def __init__(self, win = None):

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
            
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell: "Cell", undo = False):
        starting_length = abs(self._x2 - self._x1) // 2
        start_x = self._x1 + starting_length
        start_y = self._y1 + starting_length

        ending_length = abs(to_cell._x2 - to_cell._y1) // 2
        end_x = to_cell._x1 + ending_length
        end_y = to_cell._y1 + ending_length


        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        color = "gray" if undo else "red"
        self._win.draw_line(line, color)