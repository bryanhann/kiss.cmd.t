#!/usr/bin/env python3
from __my__ import my
from __my__.util import err

_GODICT = {}
_GODICT[ 'app' ]  = my.this('app')
_GODICT[ 'here' ] = my.this('here')
_GODICT[ 'repo' ] = my.repo.local.path
def go(key=None):
    try:
        my.callback.pushd( _GODICT[key] )
    except KeyError:
       err( f'arg must be in {_GODICT.keys()}' )

