# -*- coding: utf-8 -*-

"""
Created: Oct. 18th, 2018
Test file for all the sorting algorithms implemented
Author: Arthur Journe
"""

import unittest
from bubblesort import Bubblesort
from insertion_sort import InsertionSort
import random

# Test our programs

# Choose the number of tests you want to run
NumberOfTests = 1000

# Choose the maximum size of the array to sort
MaxSize = 500

class MyTest(unittest.TestCase):
    def test_BubbleSort(self):
        for i in range(NumberOfTests):
            l = [random.randint(0, 10000) for j in range(MaxSize)]
            self.assertEqual(Bubblesort(l),sorted(l))


    def test_InsertionSort(self):
        for i in range(NumberOfTests):
            l = [random.randint(0, 10000) for j in range(MaxSize)]
            self.assertEqual(InsertionSort(l), sorted(l))
