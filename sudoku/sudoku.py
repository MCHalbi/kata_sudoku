# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2023

class Sudoku:
    def __init__(self):
        self._field = [[0] * 9] * 9

    @property
    def is_solved(self) -> bool:
        return not any(0 in row for row in self._field)

    def __getitem__(self, position: tuple[int, int]) -> int:
        col_num, row_num = position
        return self._field[row_num][col_num]
