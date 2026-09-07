def fmap(fn,seq): 
    return filter(None, map( fn, seq ) )
