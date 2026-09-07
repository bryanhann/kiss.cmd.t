#!/usr/bin/env python3
def badfolder():
    pass
def goodfolder(folder):
    folder.is_dir() or folder.mkdir()
    return folder
