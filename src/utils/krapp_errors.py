from src.utils.logger import logE


class KrappError(Exception):
    """General Error class, should not be used, but who knows?"""
    message = 'Undefined KrappError'

    def __init__(self):
        logE(self.message)


class KrappErrorConnection(KrappError):
    """Connection to kRPC error, but used for network connection, not kRPC protobuf errors!"""
    message = 'Connection error!'
