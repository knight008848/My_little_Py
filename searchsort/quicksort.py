"""
Quick Sort Overview:
    ------------------------
    Uses partitioning to recursively divide and sort the list

    Time Complexity: O(n**2) worst case

    Space Complexity: O(n**2) this version

    Stable: No
"""


def sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        left, right = [], []
        for x in l[1:]:
            if x < pivot:
                left.append(x)
            elif x >= pivot:
                right.append(x)

        return sort(left) + [pivot] + sort(right)

# More simple in python
# def sort(l):
#     if len(l) <= 1:
#         return l
#     else:
#         return sort([x for x in l[1:] if x < l[0]]) + l[0] + sort([x for x in l[1:] if x >= l[0]])
