import unittest
from contextual_code_assist.main import CodeCompleter

class TestCodeCompleter(unittest.TestCase):
    def test_completion(self):
        completer = CodeCompleter()
        suggestion = completer.complete("def example_function(")
        self.assertIn(")", suggestion)

if __name__ == '__main__':
    unittest.main()