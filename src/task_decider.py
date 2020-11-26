from src.task import Task

def task_decider(task_1, task_2):
    if task_1.description == "Clean Windows" or task_2.description == "Clean Windows":
        if task_1.description == "Wash Clothes" or task_2.description == "Wash Clothes":
            return "Wash Clothes"
        elif task_1.description == "Cook Dinner" or task_2.description == "Cook Dinner":
            return "Cook Dinner"
        else:
            return "Clean Windows"
    
    elif task_1.description ==  "Wash Dishes" or task_2.description == "Wash Dishes":
        if task_1.description == "Do Ironing" or task_2.description == "Do Ironing":
            return "Do Ironing"
        elif task_1.description == "Clean Windows" or task_2.description == "Clean Windows":
            return "Clean Windows"
        else: 
            return "Wash Dishes"

    
    elif task_1.description ==  "Cook Dinner" or task_2.description == "Cook Dinner":
        if task_1.description == "Wash Dishes" or task_2.description == "Wash Dishes":
            return "Wash Dishes"
        elif task_1.description == "Wash Clothes" or task_2.description == "Wash Clothes":
            return "Wash Clothes"
        else: 
            return "Cook Dinner"

    if task_1.description == "Do Ironing" or task_2.description == "Do Ironing":
        if task_1.description == "Cook Dinner" or task_2.description == "Cook Dinner":
            return "Cook Dinner"
        elif task_1.description == "Clean Windows" or task_2.description == "Clean Windows":
            return "Clean Windows"
        else:
            return "Do Ironing"

    if task_1.description == "Wash Clothes" or task_2.description == "Wash Clothes":
        if task_1.description == "Wash Dishes" or task_2.description == "Wash Dishes":
            return "Wash Dishes"
        elif task_1.description == "Do Ironing" or task_2.description == "Do Ironing":
            return "Do Ironing"
        else:
            return "Wash Clothes"


    