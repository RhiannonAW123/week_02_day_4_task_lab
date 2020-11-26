from src.task import Task

def task_decider(task_1, task_2):
    if task_1.description == "Clean Windows" and task_2.description == "Wash Dishes":
        return "Clean Windows"
    else:
        return "Wash Dishes"

    