"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

# for example in [1,2,3,4,5], It should calculate sum of (1,3) (1,4) (1,5) (2,4) (2,5) (3,5) (1,3,5) => 9  
# in [4, 6, 0, -1, -5, 0], It should calculate sum of (4, 0) (4,-1)(4,-5) (4,0) (4, 0, -5) (4,-1,0) (6, -1) (6,-5) (6, 0) (6,-1, 0) (0, -5) (0, 0) => 5