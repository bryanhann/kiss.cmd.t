import os
from tempfile import mktemp

CALLBACK = f"{mktemp()}/callback"
NAME = 'foo'

def pytest_configure(config):
    os.environ[ "my_callback" ] = CALLBACK
    os.environ[ "my_name"     ] = NAME


