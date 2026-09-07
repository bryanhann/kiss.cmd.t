import sys
def err(text):
    if not text:
        return
    if not text.endswith('\n'):
        text = text + '\n'
    sys.stderr.write(text)
    sys.stderr.flush()
