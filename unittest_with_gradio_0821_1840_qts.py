# 代码生成时间: 2025-08-21 18:40:38
import unittest
from gradio import Interface

def add(a: int, b: int) -> int:
    """
    Function to add two integers.
    """
    return a + b

class TestAddFunction(unittest.TestCase):
    """
    Test cases for the add function.
    """
    def test_add_positive_numbers(self):
        """
        Test adding two positive numbers.
        """
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """
        Test adding two negative numbers.
        """
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative_numbers(self):
        """
        Test adding a positive and a negative number.
        "