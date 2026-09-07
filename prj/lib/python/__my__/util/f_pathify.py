from pathlib import Path

def pathify(string : str) -> Path | str:
    """If the given string looks like a path, return in as a path
    """
    if string.startswith( '/' ):
       return Path(string)
    else:
       return string
