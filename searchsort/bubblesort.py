"""
Bubble Sort Overview:
    ---------------------
    A naive sorting that compares and swaps adjacent elements

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes
"""


def sort(l):
    
    for i in range(len(l)-1):
      
        for j in range(0, len(l)-i-1):
          
            if l[j] > l[j+1]:
              
                l[j] , l[j+1] = l[j+1] , l[j]
    return l

    
def sort_1(l):

    for i in range(len(l)-1):
        
        for j in range(len(l)-1, i, -1):
          
            if l[j] < l[j-1]:
                
                l[j] , l[j-1] = l[j-1] , l[j]
    return l