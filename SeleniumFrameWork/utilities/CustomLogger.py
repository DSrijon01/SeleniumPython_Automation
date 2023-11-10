import inspect
import logging
import allure
import datetime

def customLogger():
    # 1.) This is used to get the class/method name from where this customLogger method is called
    logName = inspect.stack()[1][3]

    # 2.) Create a timestamp to use in the log file name
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # 3.) Create the logging object and append the timestamp to the logName
    logger = logging.getLogger(f"{logName}_{timestamp}")

    # 4.) Set the log level
    logger.setLevel(logging.DEBUG)

    # 5.) Create the fileHandler to save the logs in a unique file with the timestamp
    log_file = f"../reports/LogFiles/log_{timestamp}.log"
    fileHandler = logging.FileHandler(log_file, mode='a')

    # 6.) Set the log level for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # 7.) Create the formatter for the log entries
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 8.) Set the formatter for fileHandler
    fileHandler.setFormatter(formatter)

    # 9.) Add file handler to the logger
    logger.addHandler(fileHandler)

    # 10.) Return the logging object
    return logger

def allureLogs(text):
    with allure.step(text):
        pass
