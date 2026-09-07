import os

import shutil
from pathlib import Path

from __my__.OwnedObject import OwnedObject

from ..running     import run
from ..running     import leave
from ..running     import status

class LocalRepo(OwnedObject):
    @property
    def path(self): return self._boss._repopath
    @property
    def name(self): return self._owner.name
  
    def exists(self, verbose=False):
        result = self.path.exists()
        if verbose:
            return leave(self.exists, result )
        else:
            return  result
    def destroy(self, verbose=False): 
        if not self.exists():
            status(self.destroy, 'success: nothing to destroy')
            return
        status( self.destroy, 'destroying...' )
        shutil.rmtree(self.path)
        if self.exists():
            status(self.destroy, 'fail')
        else:
            status(self.destroy, 'success')

    def create(self, verbose=False): 
        run( f'gh repo clone {self.name} {self.path}' )
        self.exists(verbose=True) 
    def go(self):
        callback = self._boss.callback
        line=f"pushd {self.path}"
        input( f"{line=}")
        self._boss.callback.append(line)
    def test(self):
        self.exists() and self.destroy()
        self.create()
        self.destroy()

