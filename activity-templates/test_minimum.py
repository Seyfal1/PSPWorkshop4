"""Copy into tests/ on your assigned branch; keep this template unchanged."""
import unittest
from booking import can_book

class MinimumTests(unittest.TestCase):
    def test_negative_quantity(self):
        self.assertIs(can_book(-1, 5), False)

    def test_zero_quantity(self):
        self.assertIs(can_book(0, 5), False)

    def test_minimum_valid_quantity(self):
        self.assertIs(can_book(1, 5), True)
