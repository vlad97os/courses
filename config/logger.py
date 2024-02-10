import logging


def create_logger():
    TEST_FILE = 'test.log'
    logger = logging.Logger('courses')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(TEST_FILE)
    logger.addHandler(handler)
    return logger


log = create_logger()
