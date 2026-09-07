from __my__ import my
callback = my.callback

def test():
    """test that the callbackfile works.
    """
    callback.touch()
    lines = "#abc|#123".split('|')
    for line in lines:
        callback.append(line)
    assert lines == callback.lines()[-2:]
    print( 'pass' )

