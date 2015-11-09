"""
Selection Sort Overview:
    ------------------------
    Uses in-place comparison to sort the list

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes
"""


def sort(l):
    """Recorder the items in l from smallest to largest."""
    i = 0
    for i in range(len(l)):
        smallest = i
        j = i + 1
        while j != len(l):
            if l[j] < l[smallest]:
                # We found a smaller item at L[j]
                l[j], l[smallest] = l[smallest], l[j]
            j += 1
    return l