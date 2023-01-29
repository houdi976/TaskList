class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        status = "done" if self.is_done else "not done"
        return f"{self.name} - {status}: {self.description}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        self.tasks.append(Task(name, description))

    def mark_task_as_done(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_as_done()
                return

    def get_all_tasks(self):
        return [str(task) for task in self.tasks]

    def get_all_not_done_tasks(self):
        return [str(task) for task in self.tasks if not task.is_done]

    def get_all_done_tasks(self):
        return [str(task) for task in self.tasks if task.is_done]

task_list = TaskList()
task_list.add_task("faire projet taskList", "expliquer le code")
task_list.add_task("faire projet max rover", "expliquer choix des outils")
task_list.mark_task_as_done("projet CI")
print(task_list.get_all_tasks())
print(task_list.get_all_not_done_tasks())
print(task_list.get_all_done_tasks())
