import os
from tempfile import mktemp

CALLBACK = f"{mktemp()}/callback"
NAME = 't'

def pytest_configure(config):
    os.environ[ "my_callback" ] = CALLBACK
    os.environ[ "my_name"     ] = NAME


