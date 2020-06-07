class KrappError(Exception):
    """General Error class, should not be used, but who knows?"""
    message = 'Undefined KrappError'


class KrappErrorConnection(KrappError):
    """
    Connection to kRPC error, but used for network connection, not kRPC
    protobuf errors!
    """
    message = 'Connection error!'


class KrappErrorOSConnection(KrappError):
    """
    OS connection error, due to wrong ip or firewall, etc.
    """
    message = 'OS connection error!'
