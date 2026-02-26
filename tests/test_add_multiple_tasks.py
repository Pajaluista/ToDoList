import allure
from pages.todo_page import TodoPage


@allure.title("User can add multiple tasks")
def test_add_multiple_tasks(driver):
    page = TodoPage(driver)

    tasks = ["Buy milk", "Read book", "Write tests"]

    with allure.step("Open ToDo page"):
        page.open()

    with allure.step("Add multiple tasks"):
        for task in tasks:
            page.add_task(task)

    with allure.step("Verify all tasks are added"):
        added_tasks = page.get_tasks()
        for task in tasks:
            assert task in added_tasks