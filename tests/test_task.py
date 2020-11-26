import unittest

from src.task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("Wash Dishes", 20)
        self.task_2 = Task("Cook Dinner", 45)
        self.task_3 = Task("Clean Windows", 40)

    def test_task_desription(self):
        self.assertEqual("Wash Dishes", self.task_1.description)

    