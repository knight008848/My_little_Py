#!/usr/bin/env python3 

"""Calculate PI """

#PI = 4×(1-1/3+1/5-1/7……)
import sys
from time import clock,sleep

#Start Timer
start = clock()

n = int(sys.argv[1])

sign = 1

t = 0

for i in range(1,n+2,2):
    t += (1/i) * sign
    sign=-sign
    
s = 4 * t

finish = clock()

print ("Pi is %s" %(str(s)))
print ("Time is %.5fs" % finish)