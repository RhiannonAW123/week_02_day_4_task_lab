import unittest
from src.task import Task
from src.task_decider import task_decider

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("Wash Dishes", 20)
        self.task_2 = Task("Cook Dinner", 45)
        self.task_3 = Task("Clean Windows", 40)

    def test_task_desription(self):
        self.assertEqual("Wash Dishes", self.task_1.description)

    def test_task_duration(self):
        self.assertEqual(45, self.task_2.duration)

    def test_task_decider(self):
        self.assertEqual("Clean Windows", task_decider(self.task_3, self.task_1))