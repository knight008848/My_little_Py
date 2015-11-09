"""
 Merge Sort Overview:
    ------------------------
    Uses divide and conquer to recursively divide and sort the list

    Time Complexity: O(n log n)

    Space Complexity: O(n) Auxiliary

    Stable: Yes
"""


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]) 
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def sort(l):
    if len(l) <= 1:
        return l

    middle = int(len(l) / 2)
    left = sort(l[:middle])
    right = sort(l[middle:])
    return merge(left, right)