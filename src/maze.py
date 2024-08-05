from graph import Cell
import time, random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if seed:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
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
        self._win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(len(self._cells)-1, len(self._cells[0])-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            #right direction
            if i+1 < self._num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            #Left direction
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #top direction
            if j+1 < self._num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            #bottom direction
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            
            if not to_visit:
                return

            next_i, next_j = random.choice(to_visit)
            #right wall
            if next_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            #left wall
            if next_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            #top wall
            if next_j == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            #bottom wall
            if next_j == j - 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            self._break_walls_r(next_i, next_j)
            

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False
        