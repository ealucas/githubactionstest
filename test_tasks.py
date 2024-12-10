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
            
if __name__ == '__main__':
    unittest.main()
