class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)
    
    def incomplete(self):
        return [task for task in self.todos if not task.complete]

    def complete(self):
        return [task for task in self.todos if task.complete]

    def give_up(self):
        for task in self.todos:
            task.mark_complete()
