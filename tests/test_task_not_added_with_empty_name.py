import allure
from pages.todo_page import TodoPage


@allure.title("Task is not added when name is empty")
def test_task_not_added_with_empty_name(driver):
    page = TodoPage(driver)

    with allure.step("Open ToDo page"):
        page.open()

    with allure.step("Try to add empty task"):
        page.add_task("")

    with allure.step("Verify no tasks were added"):
        assert len(page.get_tasks()) == 0