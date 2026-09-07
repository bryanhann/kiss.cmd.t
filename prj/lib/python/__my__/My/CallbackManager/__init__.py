from __my__.OwnedObject import OwnedObject
from __my__.util import err
from pathlib import Path
class CallbackManager(OwnedObject):
    """Manage access to the callback file.
    
    There is a file that is sourced after python returns.
    """
    def touch(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch()
    @property
    def path(self):
        """Path to the callback file
        """
        return self._boss._callback

    def append(self, line):
        """Append a line to the callback file
        """
        with open( str(self.path), 'a' ) as fd:
             fd.write(line+'\n')

    def dump(self):
        print( self.path.read_text() )

    def text(self):
        """Return the text of the callback file
        """
        return self.path.read_text()

    def lines(self):
        """Return the lines of the callback file.
        """
        ret=self.path.read_text().split('\n')
        assert ret[-1]==''
        del ret[-1]
        return ret
    def pushd(self, path):
        errors=[]
        self._boss.sourced() or errors.append( 'must source' )
        Path(path).is_dir() or errors.append( 'not a dir' )
        errors = '\n'.join(errors)
        if errors:
            err(errors)
            return
        path=str(path)
        line = f"pushd {path}"
        err( line )
        self.append( f"{line} > /dev/null" )
