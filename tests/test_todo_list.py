from lib.todo_list import TodoList

"""
Initially to do list is empty
"""
def test_emty_todo_list():
    todo_list = TodoList()
    assert todo_list.todos == []