# tests/test_reference_management.py
import unittest
from utils.reference_management import generate_citation, detect_missing_references

class TestReferenceManagement(unittest.TestCase):
    def test_generate_citation(self):
        result = generate_citation("AI in Education", "John Doe", "2023", "APA")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_detect_missing_references(self):
        result = detect_missing_references("This is a sample text without references.")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_inputs(self):
        with self.assertRaises(ValueError):
            generate_citation("", "", "", "")
        with self.assertRaises(ValueError):
            detect_missing_references("")

if __name__ == "__main__":
    unittest.main()