import unittest

from src.utils.krapp_errors import KrappErrorConnection
import src.utils.logger as logger


class KrappErrorsTests(unittest.TestCase):

    def setUp(self) -> None:
        logger.init()

    def test_krapp_connection_error(self):
        self.assertEqual(KrappErrorConnection().message, 'Connection error!')


if __name__ == '__main__':
    unittest.main()
