from lib.todo_list import TodoList
from lib.todo import Todo


"""
Given we have two tasks in todo list
It reflects in the todos list
"""
def test_two_tasks_in_todos_list():
    todo_list = TodoList()
    task_1 = Todo("My task 1")
    task_2 = Todo("My task 2")
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.todos == [task_1, task_2]

"""
Given we have two tasks in todo list
And we mark complete task_1
when we call #incomplete it returns a list with task_2 in it
"""
def test_mark_complete_task1_and_return_a_list_of_task2():
    todo_list = TodoList()
    task_1 = Todo("My task 1")
    task_2 = Todo("My task 2")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    assert todo_list.incomplete() == [task_2]


