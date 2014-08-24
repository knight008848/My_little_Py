"""
Program that computes mystery number
The function returns the ratio of the number of points inside the circle divided by the total number of points. This value corresponds to the ratio of the area of the circle to the area of the square which is pi/4.
"""


import math
import random
from time import clock,sleep

def inside_unit_circle(point):
    """
    Compute distance of point from origin
    """
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return distance < 1
                                                

def estimate_mystery(num_trials):
    """
    Main function
    """
    num_inside = 0
   
    for dumm_idx in range(num_trials):
        new_point = [2 * random.random() - 1, 2 * random.random() - 1]
        if inside_unit_circle(new_point):
            num_inside += 1
   
    return (float(num_inside) / num_trials) * 4.0

start = clock()

print ("Pi is %s" %(str(estimate_mystery(10000000))))

finish = clock()

print ("Time is %.5fs" % finish)