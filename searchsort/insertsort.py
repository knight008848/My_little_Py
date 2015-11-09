"""
Insertion Sort Overview:
    ------------------------
    Uses insertion of elements in to the list to sort the list.

    Time Complexity: O(n**2)

    Space Complexity: O(n) total

    Stable: Yes
"""


def sort(l):
    """Record the values in l from smallest to largest."""
    
    i = 0
    while i != len(l):
        insert(l, i)
        i += 1

    return l


def insert(l, b):
    """ Insert l[b] where it belongs in l[0:b+1];
        l[0:b-1] must already be sorted."""
        
    # Find where to insert l[b] by searching backwards from l[b] for a smaller item.
    i = b 
    while i != 0 and l[i - 1] >= l[b]:
        i -= 1
    # Move l[b] to index i ,shifting the following values to the right.
    value = l[b]
    del l[b]
    l.insert(i, value)