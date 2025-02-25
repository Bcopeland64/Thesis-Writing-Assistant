# tests/test_proofreading.py
import unittest
from utils.proofreading import proofread

class TestProofreading(unittest.TestCase):
    def test_proofread(self):
        result = proofread("This is a sample text.")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            proofread("")

if __name__ == "__main__":
    unittest.main()