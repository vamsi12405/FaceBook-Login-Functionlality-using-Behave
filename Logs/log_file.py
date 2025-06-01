from datetime import date, datetime
import logging
import os
import allure

log_path = os.path.join(os.path.abspath(__file__ + '/../'), "current_log_file.log")

class AllureLoggingHandler(logging.Handler):
    def log(self, level_name, message):
        if callable(level_name):
            # Convert logging.info, logging.error, etc. to their names
            level_name = level_name.__name__
        elif isinstance(level_name, int):
            # Convert logging level numbers to names
            level_name = logging.getLevelName(level_name)
        if level_name.lower() == "error":
            print("ERROR:", message)
            allure.attach.file(source="C:\screenshot",attachment_type=allure.attachment_type.PNG,name="screenshot.jpg")

    def emit(self, record):
        self.log(record.levelname, record.getMessage())


def get_logs():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)", datefmt='%d/%m/%Y %I:%M:%S %p')
    allure_handler = AllureLoggingHandler()
    filehandler = logging.FileHandler(log_path, mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.addHandler(allure_handler)
    return logger


def attach_screenshot_in_report():
    driver = logging.FileHandler.selenium_driver
    current_date_time = str(f'({(date.today().strftime("%d %b"))} {(datetime.now().strftime("%H_%M_%S"))})')
    screenshot_path = os.path.join(os.path.abspath(__file__ + '/../../'), f"Failed_Screenshots/{current_date_time}.png")
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach.file(source=screenshot_path, attachment_type=allure.attachment_type.PNG, name="Screenshot")