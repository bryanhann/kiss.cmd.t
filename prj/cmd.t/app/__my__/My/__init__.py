import os
from pathlib import Path
from dataclasses import dataclass


HOME=os.getenv('HOME')
FAIL_DATA=os.getenv( 'HOME' ) + '/BCH0_DATA'
BCH0_DATA=os.getenv( 'BCH0_DATA', FAIL_DATA )
BCH0_DATA=Path(BCH0_DATA)

@dataclass
class BCH0:
    data = Path(os.getenv( 'BCH0_DATA', f'{HOME}/BCH0_DATA' ))
    tmp = Path( os.getenv( 'BCH0_TMP', f'{HOME}/BCH0_TMP' ))
    bin = Path( os.getenv( 'BCH0_BIN', f'{HOME}/BCH0_BIN' ))

def gitroot(path):
    path=Path(path)
    while not (path/'.git').exists() and not path.parent==path:
        path=path.parent
    assert (path/'.git').exists()
    return path

from .CallbackManager import CallbackManager
from .RepoManager import RepoManager    

    
def istmp(name):
    """Is the name deleteable?
    """
    name = name.replace('-','.')
    name = name.replace('_','.')
    name = name.split('.')[0].lower()
    return name in 't tmp'.split()

@dataclass 
class My: 
    """This is the root owner"""
    @property
    def ccc_istmp(self):
        name = self.name
        name = name.replace('-','.')
        name = name.replace('_','.')
        name = name.split('.')[0].lower()
        return name in 't tmp'.split()

    def this(self, name):
        key = f'this_{name}'
        try:
            return os.environ[key]
        except KeyError:
            return None
    def sourced(self):
        return self.this('fin') == 'return'
MY=My()
MY.repo      = RepoManager(MY)
MY.name      = os.environ['my_name']
MY._istmp    = istmp(MY.name)
MY.callback  = CallbackManager(MY)
MY._callback = Path(os.environ['my_callback'])
MY._root     = Path(gitroot(__file__))
MY._dname    = MY.name.replace('.','-')
MY._reponame = f'{MY._dname}.inner'
MY._repopath = BCH0.data/MY._reponame

