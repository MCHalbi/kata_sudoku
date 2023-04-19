# Author: Lukas Halbritter <halbritl@informatik.uni-freiburg.de>
# Copyright 2023
# pylint: disable=missing-docstring
import unittest
import itertools
from sudoku.sudoku import Sudoku

class SudokuTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_we_can_create_an_empty_sudoku(self):
        sudoku = Sudoku()

    def test_an_empty_sudoku_is_not_solved(self):
        sudoku = Sudoku()
        self.assertFalse(sudoku.is_solved)

    def test_field_can_be_accessed_via_index(self):
        sudoku = Sudoku()
        try:
            sudoku[0, 0]
        except Exception as exception:
            self.fail(exception)

    def test_an_empty_sudoku_has_a_zero_in_every_field(self):
        sudoku = Sudoku()
        for pos in itertools.product(range(9), repeat=2):
            with self.subTest(pos=pos):
                self.assertEqual(sudoku[pos], 0)
