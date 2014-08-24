"""
Functions to enumerate sequences of outcomes
Repetition of outcomes is allowed
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def gen_permutations(outcomes, length):
    """
    Iterative function that enumerates the set of permutations sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if new_seq.count(item) == 0:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans

def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences/gen_permutations
    if gen_permutations, return the set of Combinations
    """    
    all_sequences = gen_permutations(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

def gen_permutations_re(outcomes):
    """
    Function for generating permutations of a set of outcomes recursively
    """

    if len(outcomes) == 1:
        ans = set()
        temp = []
        temp.append(outcomes[0])
        ans.add(tuple(temp))
        return ans

    rest_permutations = gen_permutations_re(outcomes[1:])

    answer = []
    for perm in rest_permutations:
        perm = list(perm)
        for i in range(len(perm) + 1):
            temp = perm[:]
            temp.insert(i, outcomes[0])
            answer.append(tuple(temp))

    return set(answer)

# example for digits
def run_example1():
    """
    Example of all sequences
    """
    #outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(['Heads','Tails'])
    #outcomes = set(["Red", "Green", "Blue"])
    outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    
    length = 7
    seq_outcomes = gen_permutations(outcomes,length)
    print "Computed", len(seq_outcomes), "sequences of", str(length), "outcomes"
    #print "Sequences were", seq_outcomes


run_example1()


def run_example2():
    """
    Examples of sorted sequences of outcomes
    """
    # example for digits
    outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #outcomes = set(["Red", "Green", "Blue"])
    #outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    
    length = 2
    seq_outcomes = gen_all_sequences(outcomes, length)
    print "Computed", len(seq_outcomes), "sorted sequences of", str(length) ,"outcomes"
    print "Sequences were", seq_outcomes
    
run_example2()

def run_example3():
    """
    Examples of sorted sequences of outcomes
    """
    # example for digits
    #outcomes = [0, 1, 2, 3]
    #outcomes = set(["Red", "Green", "Blue"])
    outcomes = ["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    length = len(outcomes)
    seq_outcomes = gen_permutations_re(outcomes)
    print "Computed", len(seq_outcomes), "sorted sequences of", str(length) ,"outcomes"
    #print "Sequences were", seq_outcomes
    
run_example3()