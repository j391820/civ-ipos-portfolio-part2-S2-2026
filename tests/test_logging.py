from loguru import logger
import unittest


class TestTaskManager(unittest.TestCase):
    def test_logger_creates_file(self):
        logger.add