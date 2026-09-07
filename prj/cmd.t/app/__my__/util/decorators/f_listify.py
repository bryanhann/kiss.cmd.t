#!/usr/bin/env python3

def listify(fn):
    def inner(*a,**b):
        return list(fn(*a,**b))
    return inner

