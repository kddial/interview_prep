# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    # as i traverse through the indicies, 
    # keep track of the sum before the index, and after the index
    # when i move to the next index, add the index value to the before sum, 
    # and subtract it from the after sum
    before_sum = 0
    after_sum = sum(A)
    return after_sum
    

A = [-1, 3, -4, 5, 1, -6, 2, 1]
print(solution(A))