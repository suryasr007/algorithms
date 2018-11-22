"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

sum[0] = max(0, arr[0])
sum[1] = max(sum[0], arr[1])
sum[i] = max(sum[i-2] + arr[i], sum[i-1])

Follow-up: Can you do this in O(N) time and constant space?
"""

# for example in [1,2,3,4,5], It should calculate sum of (1,3) (1,4) (1,5) (2,4) (2,5) (3,5) (1,3,5) => 9
# in [4, 6, 0, -1, -5, 0], It should calculate sum of (4, 0) (4,-1)(4,-5) (4,0) (4, 0, -5) (4,-1,0) (6, -1) (6,-5) (6, 0) (6,-1, 0) (0, -5) (0, 0) => 5

def make_sets(arr, k):
    sum_ = []
    sum_.append(max(arr[0], 0))
    sum_.append(max(sum_[0], arr[1]))
    for i in range(2, len(arr)):
        sum_.append(max(sum_[i-2]+arr[i], sum_[i-1]))
    return sum_[-1]


def run():
    print(make_sets([5, 1, 1, 5], 2))

if __name__ == "__main__":
    run()