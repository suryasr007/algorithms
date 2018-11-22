"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""



def run(data, k, memo):
    if k == 0:
        return 1
    
    s = len(data) - k
    if data[s] == '0':
        return 0
    
    if memo[k] != 0:
        return memo[k]
    
    result = run(data, k-1, memo)
    if k >=2 and int(data[s:s+2]) <=26:
        result +=run(data, k-2, memo)
    memo[k] = result
    return memo


if __name__ == "__main__":
    data = '286'
    k = len(data)
    memo = [0] * (k + 1)
    print(run(data,k, memo))
