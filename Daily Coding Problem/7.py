"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""


def helper(data, k, memo):
    if k == 0:
        return 1
    
    s = len(data) - k
    if data[s] == '0':
        return 0
    
    if memo[k] != None:
        return memo[k]
    
    result = helper(data, k-1, memo)
    if k >=2 and int(data[s:s+2]) <=26:
        result +=helper(data, k-2, memo)
    memo[k] = result
    return result


def num_ways(data):
    k = len(data)
    memo = [None] * (k + 1)
    return helper(data, len(data), memo)

if __name__ == "__main__":
    print(num_ways("111"))