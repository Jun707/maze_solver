from graph import Cell
from window import Window
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._win:
            return
        pos_x1, pos_y1 = self.x1 + i * self._cell_size_x, self.y1 + j * self._cell_size_y
        pos_x2, pos_y2 = pos_x1 + self._cell_size_x, pos_y1 + self._cell_size_y

        
        self._cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)
        self._animate()

    def _animate(self):
        Window.redraw()
        time.sleep(0.1)
