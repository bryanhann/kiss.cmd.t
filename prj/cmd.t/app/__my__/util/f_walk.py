#!/usr/bin/env python3
def walk(root):
    assert root.exists()
    yield root
    if root.is_dir():
        for pth in root.glob('*'):
            yield from walk(pth)

