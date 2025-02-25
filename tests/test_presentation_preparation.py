# tests/test_presentation_preparation.py
import unittest
from utils.presentation_preparation import create_presentation_outline

class TestPresentationPreparation(unittest.TestCase):
    def test_create_presentation_outline(self):
        result = create_presentation_outline("AI in Education")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_topic(self):
        with self.assertRaises(ValueError):
            create_presentation_outline("")

if __name__ == "__main__":
    unittest.main()