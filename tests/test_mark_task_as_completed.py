import allure
from pages.todo_page import TodoPage


@allure.title("User can mark task as completed")
def test_mark_task_as_completed(driver):
    page = TodoPage(driver)

    with allure.step("Open ToDo page"):
        page.open()

    with allure.step("Add new task"):
        page.add_task("Buy milk")

    with allure.step("Mark task as completed"):
        page.complete_task("Buy milk")

    with allure.step("Verify task is marked as completed"):
        assert page.is_task_completed("Buy milk")