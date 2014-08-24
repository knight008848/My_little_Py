# http://www.codeskulptor.org/#user36_wRfQktMsHM_0.py

"""
Student code for Word Wrangler game
by Vincent
"""
##
##import urllib2
##import codeskulptor
##import poc_wrangler_provided as provided
import random

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    temp = list1[:]
    answer = []
    
    while temp:
        data = temp.pop(0)
        if len(temp) == 0:
            answer.append(data)
        else:
            if data != temp[0]:
                answer.append(data)
    return answer

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    left = list1[:]
    right = list2[:]
    answer = []

    while left and right:
        if left[0] < right[0]:
            left.pop(0)
        elif left[0] > right[0]:
            right.pop(0)
        else:
            answer.append(left.pop(0))
            right.pop(0)
            
    return answer

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """  
    left = list1[:]
    right = list2[:]
    merged = []

    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    while left:
        merged.append(left.pop(0))

    while right:
        merged.append(right.pop(0))


    return merged
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """

    # check the base
    if len(list1) <= 1:
        return list1

    # compute the midpoint
    mid = len(list1) // 2

    # split the list
    left = merge_sort(list1[:mid])
    right = merge_sort(list1[mid:])

    newList = merge(left, right)
    return newList

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    word = list(word)

    # base case
    if len(word) == 0:
        return [""]

    # recursive case
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)

    answer = []

    for item in rest_strings:
        for i in range(len(item) + 1):
            temp = item[i:] + first + item[:i]
            answer.append(temp)
        answer.append(item)        
    return answer

# Function to load words from a file

##def load_words(filename):
##    """
##    Load word list from the file named filename.
##
##    Returns a list of strings.
##    """
##
##    url = codeskulptor.file2url(filename)
##    netfile = urllib2.urlopen(url)
##
##    data = netfile.read()
##    return data
##
##def run():
##    """
##    Run game.
##    """
##    words = load_words(WORDFILE)
##    wrangler = provided.WordWrangler(words, remove_duplicates, 
##                                     intersect, merge_sort, 
##                                     gen_all_strings)
##    provided.run_game(wrangler)
##
### Uncomment when you are ready to try the game
##run()

temple = ['diff', 'effe', 'aaid', 'zfta']
l0 = gen_all_strings(temple[0])
l1 = gen_all_strings(temple[1])
l2 = gen_all_strings(temple[2])
l3 = gen_all_strings(temple[3])

l1 = merge_sort(l1)
l2 = merge_sort(l2)
l3 = merge_sort(l3)
l0 = merge_sort(l0)

print intersect(l0, l1)
print intersect(l1, l2)
print remove_duplicates(l1)

##list1 = []
##list2 = []
##for i in range(500000):
##    list1.append(random.randrange(0, 1000000))
##    list2.append(random.randrange(0, 1000000, 2))
##
##print "List Gen done!"
##
##list1 = merge_sort(list1)
##list2 = merge_sort(list2)
##
##print "List Sort done!"
##
##l3 = intersect(list1, list2)
##l4 = remove_duplicates(list1)
##l5 = remove_duplicates(list2)
##
##print len(l4), len(l5), len(list1), len(list2)
##print len(l3)









































