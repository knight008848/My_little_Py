t = 0

def memoized_fib(num, memo_dict):
    global t
    t += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

#for n in range(1,20):
#    t = 0
#    x = memoized_fib(n, {0 : 0, 1 : 1})
#    print str(n) + '->' + str(t)

def subset(outcomes):
    if len(outcomes) == 0:
        return [()]
    
    rest_permutations = subset(outcomes[1:])
    
    answer = []
    for perm in rest_permutations:

        temp = []
        temp.append(outcomes[0])
        answer.append(tuple(temp) + perm)
        answer.append(perm)
  
    return set(answer)

#list1 = [0, 1, 3]
#print subset(list1) 

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
 
    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        return merged
 
    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

print (merge_sort([2,1,3,5,7,9,2,8,0]))