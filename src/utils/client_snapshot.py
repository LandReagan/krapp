from collections import namedtuple

ClientSnapshot = namedtuple('ClientSnapshot',[
    'krpc_version',
    'connection_status',
    'body_name',
    'vessel_name'
])
