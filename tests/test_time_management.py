# tests/test_time_management.py
import unittest
from utils.time_management import create_timeline, visualize_timeline

class TestTimeManagement(unittest.TestCase):
    def test_create_timeline(self):
        tasks = ["Research", "Write Introduction", "Analyze Data"]
        result, total_days = create_timeline(tasks)
        self.assertIsInstance(result, str)
        self.assertNotEqual(result.strip(), "")
        self.assertGreater(total_days, 0)

    def test_visualize_timeline(self):
        tasks = ["Research", "Write Introduction", "Analyze Data"]
        image_path = visualize_timeline(tasks)
        self.assertTrue(image_path.endswith(".png"))

    def test_empty_tasks(self):
        with self.assertRaises(ValueError):
            create_timeline([])
        with self.assertRaises(ValueError):
            visualize_timeline([])

if __name__ == "__main__":
    unittest.main()