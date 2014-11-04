#!/usr/bin/env python

import unittest

import os
from sys import argv, exit, stdout
from time import time, localtime
ow=stdout.write

from binary_search import binary_search
from selectsort import selection_Sort
from insertsort import insertion_Sort
from bubblesort import bubble_Sort_1
from bubblesort import bubble_Sort_2

VALUES = [ 5982, 3882, 3482, 4324, 9399, 2631, 8012, 2925, 2542, 4272, 
           3854, 1650, 3673, 5854, 3039, 2937,  744, 6265, 9230,  772,
           2627, 9555, 4190, 2166, 2851, 5971, 8127, 7285, 5396, 4997,
           4874, 5392, 6729,  399, 6621, 3523, 7937, 6855, 2360, 7993,
           8089, 9043, 8951, 2721,  194, 5553, 1393, 6164, 3204, 5273]


def main(argv):
    # key = int(argv[1])

     
    t1 = time()
    bubble_Sort_2(VALUES)
    t2 = time()
    Total = (t2 - t1) * 1000

    ow ('='*64 + '\n')
    for i in range(50):
        ow ("%5d" % VALUES[i])
        if ((i+1) % 10) == 0 :
            ow("\n") 
    
    ow ('='*64 + '\n')
    ow ("Sort finished in %.4f ms.\n" % Total)


if __name__ == "__main__":
    main(argv)
