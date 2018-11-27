def hourglassSum(arr):   
    sums = []
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[i]) - 2):
            sums.append(sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))
    return max(sums)

res = hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])

print(res)
