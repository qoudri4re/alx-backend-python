#!/usr/bin/env python3
"""
contains a function takes a 
list input_list of floats as 
argument and returns their sum as 
a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''computes the sum of the list'''
    return float(sum(input_list))
