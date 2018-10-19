# -*- coding: utf-8 -*-

"""
Created: Oct. 18th, 2018
Implementation of the well-known insertion sort
Author: Arthur Journe
"""

# Type of algorithm: Sorting algorithm
# Complexity: 0(n²)
# Efficient for: small lists/1D-arrays

import unittest

def InsertionSort(array):
    """
        Sorts an array using the insertion sort algorithm
        Input: array, 1D
        Output; the same array, sorted
    """

    for ind, elt in enumerate(array):
        i = ind -1
        while i >= 0 and array[i]>elt:
            array[i+1] = array[i]
            i-=1
        array[i+1] = elt

    return array
