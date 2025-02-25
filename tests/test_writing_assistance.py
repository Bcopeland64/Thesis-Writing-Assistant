# tests/test_writing_assistance.py
import unittest
from utils.writing_assistance import improve_writing, check_logical_flow

class TestWritingAssistance(unittest.TestCase):
    def test_improve_writing(self):
        result = improve_writing("This is a sample text.", tone="academic", audience="academic")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_check_logical_flow(self):
        result = check_logical_flow("This is a sample text.")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            improve_writing("")
        with self.assertRaises(ValueError):
            check_logical_flow("")

if __name__ == "__main__":
    unittest.main()