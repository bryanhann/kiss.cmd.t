from pathlib import Path
HOME=Path.home()
(HOME/'foo').touch
print( f'{HOME=}' )
for nn, name in enumerate(HOME.glob('*')):
    print( nn, name )
