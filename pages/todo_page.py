from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TodoPage:

    URL = "https://crossbrowsertesting.github.io/todo-app.html"

    TASK_INPUT = (By.ID, "todotext")
    ADD_BUTTON = (By.ID, "addbutton")
    TASKS = (By.CSS_SELECTOR, "ul li")
    ARCHIVE_BUTTON = (By.LINK_TEXT, "archive")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def add_task(self, task_name):
        self.driver.find_element(*self.TASK_INPUT).clear()
        self.driver.find_element(*self.TASK_INPUT).send_keys(task_name)
        self.driver.find_element(*self.ADD_BUTTON).click()

    def get_tasks(self):
        return [task.text for task in self.driver.find_elements(*self.TASKS)]

    def mark_task_completed(self, task_name):
        tasks = self.driver.find_elements(*self.TASKS)
        for task in tasks:
            if task.text == task_name:
                checkbox = task.find_element(By.TAG_NAME, "input")
                checkbox.click()

    def archive_completed(self):
        self.driver.find_element(*self.ARCHIVE_BUTTON).click()

    TASK_LABELS = (By.CSS_SELECTOR, "ul.todo-list li label")
    TASK_CHECKBOXES = (By.CSS_SELECTOR, "ul.todo-list li input.toggle")

    def complete_task(self, task_name):
        # ждем, пока хотя бы один li появится
        tasks = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul li"))
        )
        for task in tasks:
            text_elem = task.find_element(By.CSS_SELECTOR, "span")  # span внутри li содержит текст
            if text_elem.text == task_name:
                checkbox = task.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
                checkbox.click()
                break

    def is_task_completed(self, task_name):
        tasks = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul li"))
        )
        for task in tasks:
            text_elem = task.find_element(By.CSS_SELECTOR, "span")
            if text_elem.text == task_name:
                return "completed" in task.get_attribute("class")
        return False