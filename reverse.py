# -*- coding: utf-8 -*-

def rev_args(func):
    def deco(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return deco

