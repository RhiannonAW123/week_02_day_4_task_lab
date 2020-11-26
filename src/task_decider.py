from src.task import Task

def task_decider(task_1, task_2):
    if task_1.description == "Clean Windows" or task_2.description == "Clean Windows":
        if task_1.description == "Wash Dishes" or task_2.description == "Wash Dishes":
            return "Clean Windows"
        else:
            return "Cook Dinner"
    
    elif task_1.description ==  "Wash Dishes" or task_2.description == "Wash Dishes":
        if task_1.description == "Cook Dinner" or task_2.description == "Cook Dinner":
            return "Wash Dishes"
        else: 
            return "Clean Windows"

    
    elif task_1.description ==  "Cook Dinner" or task_2.description == "Cook Dinner":
        if task_1.description == "Clean Windows" or task_2.description == "Clean Windows":
            return "Cook Dinner"
        else: 
            return "Wash Dishes"


    