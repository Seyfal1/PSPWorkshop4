"""Existing checks: these deliberately do not cover the missing rules."""
import unittest
from booking import can_book

class BaselineTests(unittest.TestCase):
    def test_one_place_with_capacity(self):
        self.assertIs(can_book(1, 5), True)

    def test_request_within_capacity(self):
        self.assertIs(can_book(2, 5), True)

    def test_exact_capacity(self):
        self.assertIs(can_book(5, 5), True)

if __name__ == '__main__':
    unittest.main()
