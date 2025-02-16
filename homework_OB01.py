class Task: #Создаем класс
    def __init__(self, description, due_date): #Конструктор
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self): #Метод
        self.completed = True

    def __str__(self): #Метод
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager: #Создаем класс
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date): #Метод
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def mark_task_as_completed(self, description): #Метод
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f"Задача отмечена как выполненная: {task}")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    def show_current_tasks(self): #Метод
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи (не выполненные):")
            for task in current_tasks:
                print(task)
        else:
            print("Нет текущих задач.")

# Создаем менеджер задач
manager = TaskManager()

# Добавляем задачи
manager.add_task("Купить молоко", "16/02/2025")
manager.add_task("Позвонить другу", "16/02/2025")
manager.add_task("Сделать домашнее задание", "16/02/2025")

# Отмечаем задачу как выполненую
manager.mark_task_as_completed("Сделать домашнее задание")

# Показываем текущие задачи
manager.show_current_tasks()