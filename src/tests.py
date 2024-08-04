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
        maze1.break_entrance_and_exit()
        self.assertEqual(maze1._cells[0][0].has_top_wall, False)
        self.assertEqual(maze1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)

    

if __name__ == "__main__":
    unittest.main()