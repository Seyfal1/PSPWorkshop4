"""Copy into tests/ on your assigned branch; keep this template unchanged."""
import unittest
from booking import can_book

class CapacityTests(unittest.TestCase):
    def test_above_capacity(self):
        self.assertIs(can_book(6, 5), False)

    def test_no_capacity(self):
        self.assertIs(can_book(1, 0), False)

    def test_exact_capacity(self):
        self.assertIs(can_book(5, 5), True)
