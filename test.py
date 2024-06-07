from unittest.mock import patch
import unittest
from unittest.mock import patch
from src.code_runner import CodeRunner


class TestCodeRunnerIntegration(unittest.TestCase):
    def setUp(self):
        self.code_runner = CodeRunner(True, False, 9, "BADTIE", "generated_tests", 10, 1)

    @patch('src.code_runner.TestGenerator.generate_test')
    def test_check_test_integration(self, mock_generate_test):
        acc = """
def patched_func(a, b):
    if b == 0:
        return a
    else:
        return patched_func(b, a % b)
"""

        rej = """
def original_func(a,b):
    if b==0:
        return a
    else:
        return original_func(a,a%b)
"""
        existing_test = {'inputdata': [17, 0]}
        mock_generate_test.return_value = [["\n{'inputdata': [12, 18]}\n"], ["\n{'inputdata': [12, 18]}\n"], ["\n{'inputdata': [25, 5]}\n"], ["\n{'inputdata': [12, 18]}\n"], [
            "{'inputdata': [10, 5]}"], ["\n{'inputdata': [12, 8]}\n"], ["\n{'inputdata': [48, 18]}\n"], ["{'inputdata': [12, 8]}"], ["\n{'inputdata': [36, 48]}\n"], ["\n{'inputdata': [30, 12]}\n"]]

        res = self.code_runner.check_test(
            acc, rej, existing_test, 'program_name', 'program_name')

        self.assertEqual(res, "Found1")

if __name__ == '__main__':
    unittest.main()
