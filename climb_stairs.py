def climb(n):
    result = [1,1]
    if n >= 2:
        for i in range(2,n+1):
            result.append(result[i-1]+result[i-2])
    return result[n]

print(climb(13))