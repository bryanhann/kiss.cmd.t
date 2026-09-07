
from __my__.OwnedObject import OwnedObject

from ..running import run
from ..running import listrepos
from ..running import leave, status, success

class RemoteRepo(OwnedObject):
    @property
    def name(self):
        return self._boss._reponame

    def create(self, verbose=False, check=False):
        if check:
            status( self.create, 'checking whether repo exists' )
            if self.exists():
                return success( self.create, True )
        else:
            status( self.create, 'no checking' )
        status( self.create, 'creating repo' )
        line = f'gh repo create {self.name} --private'
        run(line, verbose=verbose)
        if check:
            return success( self.create, self.exists() )
            #if self.exists():
            #    status( self.create, 'success' )
            #else:
            #    status( self.create, 'failure' )
    def destroy(self, yes=False, verbose=False):
        yes = '--yes' if yes or self._boss._istmp else ''
        line = f'gh repo delete {self.name} {yes}'
        run(line, verbose=verbose)
    def exists(self):
        result = self.name in listrepos()
        leave( self.exists, result )
        return result
    def test(self, yes=False):
        self.destroy()
        self.create()
        self.destroy()



