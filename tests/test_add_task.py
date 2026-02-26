import allure
from pages.todo_page import TodoPage


def test_add_task_valid_name(driver):
    page = TodoPage(driver)
    page.open()

    page.add_task("Buy milk")

    assert "Buy milk" in page.get_tasks()