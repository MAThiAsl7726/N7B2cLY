# 代码生成时间: 2025-08-03 15:32:09
import unittest
import gr

# Define your functions that you want to test

def add(a, b):
    """
    Adds two numbers and returns the sum
    """
    return a + b


def subtract(a, b):
    """
    Subtracts b from a and returns the result
    """
    return a - b

# Define test cases for your functions
class ArithmeticTests(unittest.TestCase):
    """
    Test cases for arithmetic operations
    """
    def test_add(self):
        """
        Verify that add function works correctly
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """
        Verify that subtract function works correctly
        """
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-1, 1), -2)

# Create a Gradio interface for running tests
def run_tests():
    """
    Runs all test cases and prints the results
    """
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ArithmeticTests)
    test_result = unittest.TextTestRunner().run(test_suite)

    # Check if there were any failures or errors
    failures = len(test_result.failures)
    errors = len(test_result.errors)
    if failures + errors == 0:
        return "All tests passed!"
    else:
        return f"{failures + errors} tests failed."

# Create a Gradio interface
iface = gr.Interface(
    run_tests,
    inputs=[],
    outputs="text",
    title="Unit Testing Framework with Gradio",
    description="This interface allows you to run unit tests for arithmetic operations."
).launch()
