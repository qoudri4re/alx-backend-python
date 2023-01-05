#!/usr/bin/env python3
"""
contains a function  takes a string k 
and an int OR float v as 
arguments and returns a tuple.
"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''logic'''
    return (k, float(v**2))
