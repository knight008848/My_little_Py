"""
Shell Sort Overview:
    ------------------------
    Comparison sort that sorts far away elements first to sort the list

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes
"""


def sort(l):

    gaps = [x for x in range(len(l) / 2, 0, -1)]

    for gap in gaps:
        for i in range(gap, len(l)):
            temp = l[i]
            j = i 
            while j >= gap and l[j-gap] > temp:
                l[j] = l[j-gap]
                j -= gap
            l[j] = temp
    return l