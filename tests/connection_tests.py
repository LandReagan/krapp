import unittest

import src.utils.logger as logger
import src.connection.client as _client
from utils.krapp_errors import KrappErrorConnection


class ConnectionTests(unittest.TestCase):

    def setUp(self) -> None:
        logger.init()

    def test_empty_connection(self):
        self.assertRaises(KrappErrorConnection, _client.connect())

    def test_connection(self):
        _client.connect('192.168.100.151')
        self.assertIsNotNone(_client)


if __name__ == '__main__':
    unittest.main()
