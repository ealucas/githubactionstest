import unittest
from main import *
class TestTask(unittest.TestCase):
    def test_initialization(self):
            task = Task("Test Task", priority="High", deadline="2024-12-31")
            self.assertEqual(task.description, "Test Task")
            self.assertEqual(task.priority, "High")
            self.assertEqual(task.deadline, "2024-12-31")
            self.assertFalse(task.completed)

    def test_mark_done(self):
            task = Task("Test Task", priority="High", deadline="2024-12-31")
            self.assertFalse(task.completed)
            task.mark_done()
            self.assertTrue(task.completed)
    def test_set_due(self):
            task = Task(*"Test Task", priority="Low", deadline="2024-12-21")
            task.set_due("2025-12-21")
            task.assertEqual(task.deadline, "2025-12-21")
if __name__ == '__main__':
    unittest.main()
