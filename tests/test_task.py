import unittest
from src.task import Task
from src.task_decider import task_decider

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("Wash Dishes", 20)
        self.task_2 = Task("Cook Dinner", 45)
        self.task_3 = Task("Clean Windows", 40)
        self.task_4 = Task("Do Ironing", 40)
        self.task_5 = Task("Wash Clothes", 60)

    def test_task_desription(self):
        self.assertEqual("Wash Dishes", self.task_1.description)

    def test_task_duration(self):
        self.assertEqual(45, self.task_2.duration)

    def test_task_decider__returns_clean_windows(self):
        self.assertEqual("Clean Windows", task_decider(self.task_3, self.task_1))

    def test_task_decider__returns_wash_dishes(self):
        self.assertEqual("Wash Dishes", task_decider(self.task_1, self.task_2))

    def test_task_decider__returns_cook_dinner(self):
        self.assertEqual("Cook Dinner", task_decider(self.task_3, self.task_2))

    def test_task_decider__returns_clean_windows_reversed(self):
        self.assertEqual("Clean Windows", task_decider(self.task_1, self.task_3))
    
    def test_task_decider__wash_dishes_wash_clothes(self):
        self.assertEqual("Wash Dishes", task_decider(self.task_1, self.task_5))

    def test_task_decider__wash_clothes_cook_dinner(self):
        self.assertEqual("Wash Clothes", task_decider(self.task_5, self.task_2))
    

    
