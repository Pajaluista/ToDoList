import allure
from pages.todo_page import TodoPage

@allure.title("Add two tasks")
def test_add_two_tasks(driver):
    page = TodoPage(driver)
    page.open()

    task1 = "Task 1"
    task2 = "Task 2"

    with allure.step("Add first task"):
        page.add_task(task1)

    with allure.step("Add second task"):
        page.add_task(task2)

    with allure.step("Verify both tasks are in the list"):
        tasks = page.get_tasks()
        assert task1 in tasks
        assert task2 in tasks