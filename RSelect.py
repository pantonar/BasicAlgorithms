#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:37:35 2020

@author: pablo

Rselect implementation
"""
import numpy as np

def Rselect(a, i):
    '''
    Arguments:
        a -- list of distinct numbers
        i -- integer
    Returns:
        the ith order statistic  (ith smallest element of an input array)
    '''
    n =len(a)
    print(f"n is {n}, i is {i}")
    print(a)
    if n == 1:
        stat=a[0]
        return stat
    else:
        p = Pivot(n)
        Swap(a, 0, p)
        j = Partition(a)
        print(f"j is {j}")
        if j+1 == i:
            stat =a[j]
            return stat
        elif j>i-1:
            stat = Rselect(a[:j], i)
        else:
            stat = Rselect(a[j+1:], i-j-1)
    return stat




def Pivot(n):
    '''return a random integer in the rang of n'''
    return np.random.randint(n)

def Swap(a, i, j):
    '''swap a[i] with a[j]'''
    a[i], a[j] = a[j], a[i]
    return

def Partition(a):
    '''In-place partition subroutine'''
    i=1
    p=a[0]
    for j in range(1, len(a)):
        if a[j]<p:
            Swap(a, i,j)
            i+=1
    Swap(a, 0, i-1)
    return i-1
            
# testing with a random array
a = np.random.randint(20, size =10)
b=a.copy()
q = Rselect(a, 3)
