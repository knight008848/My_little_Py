#!/usr/bin/env python

'''
Fibonacci number in Pure Python
=============================
In mathematics, the Fibonacci numbers are the numbers in the following integer sequence:
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....
By definition, the first two Fibonacci numbers are 0 and 1, and each subsequent number is the sum of the previous two.

Usage:

fib(n) 输出n的Fibonacci数 
fib2(n) 返回所有小于n的Fibonacci数

License: 
    GNU General Public License (GPL, see [url]http://www.gnu.org[/url]).
    In short, users are free to use and distribute this program
    in whole. If users make revisions and distribute the revised
    one, they are required to keep the revised source accessible
    to the public.
    
Version:

    0.1.0,  August/08/2011 Initial release    
       
'''

__version__ = "0.1.0"

import os
import math


def fib_help():
    print(__doc__)

def fib(n):
    """fib(n) 输出n的Fibonacci数"""
    curr, next = 0, 1
    while(n):
        curr, next, n = next, curr+next, n-1
    return x
    
def fib2(n):
    """fib2(n) 返回所有小于n的Fibonacci数"""
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b,a+b
    return result
    
def Pascal_triangle(m, n):
    return int(math.factorial(m-1) / math.factorial(m-n) /math.factorial(n-1))
    
    
    
#def fibonacci(n):
#    if n < 2:
#        return n
#    else:
#        return fibonacci(n-2) + fibonacci(n-1)