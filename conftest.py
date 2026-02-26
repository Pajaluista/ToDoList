import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pytest


@pytest.fixture
def driver():
    options = Options()

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)