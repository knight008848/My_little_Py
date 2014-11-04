def selection_Sort(L):
    """Recorder the items in L from smallest to largest."""
    i = 0
    for i in range(len(L)):
        smallest = i
        j = i + 1
        while j != len(L):
            if L[j] < L[smallest]:
                # We found a smaller item at L[j]
                L[j],L[smallest] = L[smallest],L[j]
            j = j + 1