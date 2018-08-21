
#先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶
#f(n) = f(n-1) + f(n-2)
def climb(n):
    dp = [1 for i in range(n+1)]
    print(dp)
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]





print(climb(13))
