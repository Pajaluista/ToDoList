import allure
from pages.todo_page import TodoPage

@allure.title("Add single task")
def test_add_single_task(driver):
    page = TodoPage(driver)
    page.open()

    task_name = "Buy milk"

    with allure.step("Add task"):
        page.add_task(task_name)

    with allure.step("Verify task is in the list"):
        tasks = page.get_tasks()
        assert task_name in tasks