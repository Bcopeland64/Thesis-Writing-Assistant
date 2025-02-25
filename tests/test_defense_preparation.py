# tests/test_defense_preparation.py
import unittest
from utils.defense_preparation import get_defense_questions, prepare_responses

class TestDefensePreparation(unittest.TestCase):
    def test_get_defense_questions(self):
        result = get_defense_questions()
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_prepare_responses(self):
        result = prepare_responses("This is a sample response.")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_response(self):
        with self.assertRaises(ValueError):
            prepare_responses("")

if __name__ == "__main__":
    unittest.main()