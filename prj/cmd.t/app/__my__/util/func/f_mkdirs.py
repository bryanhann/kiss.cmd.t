#!/usr/bin/env python3
from pathlib import Path
def mkdirs(path):
    path=Path(path)
    if not path.is_dir():
        mkdirs(path.parent)
        path.mkdir() 
    return path


