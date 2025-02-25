# tests/test_thesis_structure.py
import unittest
from utils.thesis_structure import generate_outline

class TestThesisStructure(unittest.TestCase):
    def test_generate_outline(self):
        result = generate_outline("APA")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_unsupported_format(self):
        with self.assertRaises(ValueError):
            generate_outline("UnsupportedStyle")

if __name__ == "__main__":
    unittest.main()