from pages.todo_page import TodoPage


def test_delete_task(driver):
    page = TodoPage(driver)
    page.open()

    page.add_task("Delete me")
    page.mark_task_completed("Delete me")
    page.archive_completed()

    assert "Delete me" not in page.get_tasks()