#!/usr/bin/env python

'''
Eight queens puzzle in Pure Python
=============================
The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard 
so that no two queens attack each other. Thus, a solution requires that no two queens share 
the same row, column, or diagonal. 
The eight queens puzzle is an example of the more general n-queens problem of placing n queens 
on an n×n chessboard, where solutions exist for all natural numbers n with the exception of 2 and 3.

The eight queens puzzle has 92 distinct solutions. If solutions that differ only by symmetry operations
(rotations and reflections) of the board are counted as one, the puzzle has 12 unique (or fundamental) solutions.

With the solution represented as a vector with one queen in each row, 
we don't have to check to see if two queens are on the same row. 
By using a permutation generator, we know that no value in the vector is repeated, 
so we don't have to check to see if two queens are on the same column. 
Since rook moves don't need to be checked, we only need to check bishop moves.
The technique for checking the diagonals is to add or subtract the column number from each entry, 
so any two entries on the same diagonal will have the same value (in other words, the sum or difference is unique for each diagnonal). 
Now all we have to do is make sure that the diagonals for each of the eight queens are distinct. 
So, we put them in a set (which eliminates duplicates) and check that the set length is eight (no duplicates were removed).
Any permutation with non-overlapping diagonals is a solution. So, we print it and continue checking other permutations.

http://en.wikipedia.org/wiki/Eight_queens_puzzle
http://code.activestate.com/recipes/576647/

License: 
    GNU General Public License (GPL, see [url]http://www.gnu.org[/url]).
    In short, users are free to use and distribute this program
    in whole. If users make revisions and distribute the revised
    one, they are required to keep the revised source accessible
    to the public.
    
Version:

    0.1.0,  August/18/2011 Initial release    
       
'''

from itertools import permutations
 
n = 8
cols = range(n)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        result = ('a'+str(vec[0]+1),'b'+str(vec[1]+1),'c'+str(vec[2]+1),'d'+str(vec[3]+1),'e'+str(vec[4]+1),'f'+str(vec[5]+1),'g'+str(vec[6]+1),'h'+str(vec[7]+1))      
        print (result)
