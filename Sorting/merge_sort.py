# -*- coding: utf-8 -*-

"""
Created: Oct. 18th, 2018
Implementation of the merge sort algorithm
Author: Arthur Journe
"""

#Type: Sorting algorithm, divide and conquer
# Complexity: O(nlog(n))
#Efficient for: very efficient
from math import inf

def merge(array1, array2):
    # Merge the 2 sorted arrays
    n1 = len(array1)
    n2 = len(array2)
    array1.append(inf)
    array2.append(inf)
    i = 0
    j = 0

    final_array_sorted = []
    for k in range(n1 + n2):
        if array1[i] <= array2[j]:
            final_array_sorted.append(array1[i])
            i+=1
        else:
            final_array_sorted.append(array2[j])
            j+=1
    return final_array_sorted


def MergeSort(array):
    if len(array) == 1:
        return array
    else:
        q = int(len(array)/2)
        return(merge(MergeSort(array[:q]), MergeSort(array[q:])))
