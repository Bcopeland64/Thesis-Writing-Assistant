# tests/test_methodology_guidance.py
import unittest
from utils.methodology_guidance import suggest_methodology, suggest_data_collection

class TestMethodologyGuidance(unittest.TestCase):
    def test_suggest_methodology(self):
        result = suggest_methodology("How does AI impact education?")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_suggest_data_collection(self):
        result = suggest_data_collection("Qualitative Research")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            suggest_methodology("")
        with self.assertRaises(ValueError):
            suggest_data_collection("")

if __name__ == "__main__":
    unittest.main()