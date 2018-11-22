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

    # for i in range(2, len(num) + 1):
    #     count[i] = 0

    #     if num[i-1] > '0':
    #         count[i] = count[i-1]

    #     if num[i-2] == '1' or (num[i-2] == '2' and num[i-1] < '7'):
    #         count[i] += count[i-2]
    # return count[len(num)]

    #     # result.append(''.join(temp_result))
        
    # print(result)

if __name__ == "__main__":
    data = '286'
    k = len(data)
    memo = [0] * (k + 1)
    print(run('345',k, memo))
