import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 5
        num_rows = 5
        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze1._cells), num_cols, )
        self.assertEqual(len(maze1._cells[0]), num_rows, )

    def test_maze_entrance_exit_no_wall(self):
        num_cols = 5
        num_rows = 5
        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(maze1._cells[0][0].has_top_wall, False)
        self.assertEqual(maze1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)
    
    def test_maze_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(maze1._cells[i][j].visited, False)
    

if __name__ == "__main__":
    unittest.main()