def binary_search(v,L):
        """Return the index of the leftmost occurrence of v in list L, or -1 if v is not in L."""
        # Mark the left and right indices of the unknown section
        low = 0
        high = len(L) - 1
        
        while low != high + 1 :
            
            mid = (low + high) // 2
            #print("i=%d,j=%d,m=%d\n" % (i,j,m))
            if L[mid] < v:
                low = mid + 1
            else:
                high = mid - 1
        
        if 0 <= low < len(L) and L[low] == v :
            return i
        else :
            return -1