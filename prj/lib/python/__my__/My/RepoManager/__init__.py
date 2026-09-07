from .LocalRepo  import LocalRepo
from .RemoteRepo import RemoteRepo
from __my__.OwnedObject import OwnedObject

class RepoManager(OwnedObject):
    @property
    def local(self):
        return LocalRepo(self)
    @property
    def remote(self): 
        return RemoteRepo(self)

    @property
    def name(self): 
        dot=self._boss.name
        dash = dot.replace('.', '-')
        return f'{dash}.inner'

    def install(self):
        """Install the repos for this app

        More info
        """
        self.remote.create()
        self.local.create()
    @property
    def _path(self): return self._boss._repopath
