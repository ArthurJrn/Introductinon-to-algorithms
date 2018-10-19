# -*- coding: utf-8 -*-

"""
Created: Oct. 18th, 2018
Implementation of the well-known bubblesort algorithm
Author: Arthur Journe
"""

#Type: Sorting algorithm
# Complexity: O(n²)
#Efficient for: small arrays, pretty inefficient
import unittest

def Bubblesort(array):
    """
        Sorts an array using the bublesort algorithm
        Input: array, 1D
        Output: the same array, sorted
    """
    n = len(array)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
    return array
