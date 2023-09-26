class Todo:
    def __init__(self, task):
        self.task = task
        self.complete_task = False

    def mark_complete(self):
        self.complete_task = True

