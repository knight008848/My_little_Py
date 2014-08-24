http://www.codeskulptor.org/#user36_wRfQktMsHM_0.py

"""
Student code for Word Wrangler game
by Vincent
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    answer = []
    for item in list1:
    
        if answer.count(item) == 0:
            answer.append(item)
          
    return answer

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """

    answer = []

    for item in list1:
        if list2.count(item) > 0:
            answer.append(item)


    return answer

# Functions to perform merge sort

def merge(left, right):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """  

    merged = []

    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    while left:
        merged.append(left[0])

    while right:
        merged.append(right[0])


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
    # base case
    if len(word) == 0:
        return [""]

    # recursive case
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)

    answer = []

    for item in rest_strings:
        for dummy_idx in range(len(item) + 1):
            temp = list(item)
            temp.insert(i, first)
            answer.append(str(temp))
        answer.append(item)        
    return answer

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """

    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)

    data = netfile.read()
    return data

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    
