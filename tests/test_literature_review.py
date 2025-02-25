# tests/test_literature_review.py
import unittest
from utils.literature_review import search_literature, summarize_paper

class TestLiteratureReview(unittest.TestCase):
    def test_search_literature(self):
        result = search_literature("AI in Education")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_summarize_paper(self):
        result = summarize_paper("The Impact of AI on Education")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            search_literature("")
        with self.assertRaises(ValueError):
            summarize_paper("")

if __name__ == "__main__":
    unittest.main()